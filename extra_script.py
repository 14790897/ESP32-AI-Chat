# extra_script.py
import subprocess
import sys
from SCons.Script import AlwaysBuild, Default, DefaultEnvironment, Exit

Import("env")


# 可以考虑添加一个仅构建和上传文件系统的目标
env.AddCustomTarget(
    name="build_upload_fs",
    dependencies=None,
    actions=lambda source, target, env: [
        env.Execute(
            f'$PYTHONEXE -m platformio run --target buildfs --environment {env["PIOENV"]}'
        ),
        env.Execute(
            f'$PYTHONEXE -m platformio run --target uploadfs --environment {env["PIOENV"]}'
        ),
    ],
    title="Build & Upload Filesystem",
    description="Build and then upload the filesystem image",
)
