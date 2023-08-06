import os
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Dict, List, Union

import typer
from tqdm.contrib.concurrent import process_map

from zod.cli.download import Version
from zod.cli.utils import SubDataset
from zod.data_classes.info import Information

app = typer.Typer(help="ZOD Download Verifyer", no_args_is_help=True)


def _verify_info(
    info: Information, separate_lidar: bool
) -> Dict[str, Dict[str, Union[bool, List[bool]]]]:
    """Verify the given infos."""
    stats = defaultdict(dict)
    stats["general"] = {
        "calibration": os.path.exists(info.calibration_path),
        "ego_motion": os.path.exists(info.ego_motion_path),
        "metadata": os.path.exists(info.metadata_path),
        "oxts": os.path.exists(info.oxts_path),
    }
    if info.vehicle_data_path is not None:
        stats["general"]["vehicle_data"] = os.path.exists(info.vehicle_data_path)
    for annotation in info.annotations.values():
        stats["annotations"][annotation.project.value] = os.path.exists(annotation.filepath)
    for lidar, lidar_frames in info.lidar_frames.items():
        for i, lidar_frame in enumerate(lidar_frames):
            exists = os.path.exists(lidar_frame.filepath)
            name = lidar.value
            if separate_lidar:
                index = i - len(lidar_frames) // 2
                if index < 0:
                    name += f"_{-index:02d}_before"
                elif index > 0:
                    name += f"_{index:02d}_after"
                else:
                    name += "_core"
                stats["lidar"][name] = exists
            else:
                if name not in stats:
                    stats["lidar"][name] = []
                stats["lidar"][name].append(exists)
    for camera, camera_frames in info.camera_frames.items():
        stats["camera"][camera] = []
        for camera_frame in camera_frames:
            stats["camera"][camera].append(os.path.exists(camera_frame.filepath))
    return stats


def _print_results(verified_infos):
    groups = sorted(set().union(*verified_infos))
    for group in groups:
        keys = sorted(set().union(*(v[group] for v in verified_infos)))
        stats = {
            k: [d[group][k] for d in verified_infos if group in d and k in d[group]] for k in keys
        }
        print(f"\n\n{group.upper():^45}\n{'-' * 50}")
        print(f"{'Data':<20} {'Downloaded (%)':<15} {'Expected (count)':<15}")
        print("-" * 50)
        for data_name, data_stats in stats.items():
            if isinstance(data_stats[0], bool):
                successes = sum(data_stats)
                totals = len(data_stats)
            else:  # list
                successes = sum(sum(substats) for substats in data_stats)
                totals = sum(len(substats) for substats in data_stats)
            percentage = 100 * successes / totals
            print(f"{data_name:<20} {percentage:<15.2f} {totals:<15}")


@app.command(no_args_is_help=True)
def verify(
    dataset_root: Path = typer.Option(..., help="Dataset directory"),
    subset: SubDataset = typer.Option(..., help="The sub-dataset to verify"),
    version: Version = typer.Option(..., help="The version of the dataset to verify"),
):
    """Verify the downloaded files."""
    zod = subset.dataset_cls(str(dataset_root.expanduser()), version.value)
    infos = zod.get_all_infos()
    verified_infos = process_map(
        partial(_verify_info, separate_lidar=subset == SubDataset.FRAMES),
        infos.values(),
        chunksize=1 if version == "mini" else min(len(infos) // 100, 100),
        desc="Verifying files...",
    )
    _print_results(verified_infos)


if __name__ == "__main__":
    app()
