# extra_script.py
import subprocess
import sys
from SCons.Script import AlwaysBuild, Default, DefaultEnvironment, Exit

# 导入当前的构建环境
Import("env")  # noqa: F821


# 定义一个函数，该函数将按顺序执行上传操作
def upload_all_action(source, target, env):
    # ... (函数内容保持不变) ...
    print("--- Running Custom Target: upload_all ---")

    env_name = env["PIOENV"]
    print(f"Targeting environment: {env_name}")

    print("\nSTEP 1: Uploading firmware...")
    try:
        fw_upload_cmd = [
            env.subst("$PYTHONEXE"),
            "-m",
            "platformio",
            "run",
            "--target",
            "upload",
            "--environment",
            env_name,
        ]
        print(f"Executing: {' '.join(fw_upload_cmd)}")
        subprocess.run(fw_upload_cmd, check=True, text=True, capture_output=False)
        print("STEP 1: Firmware upload successful.")
    except subprocess.CalledProcessError as e:
        print(
            f"ERROR during firmware upload step: Command exited with status {e.returncode}"
        )
        print("Aborting upload_all.")
        Exit(1)
    except Exception as e:
        print(f"ERROR during firmware upload step: {e}")
        print("Aborting upload_all.")
        Exit(1)

    print("\nSTEP 2: Uploading filesystem image...")
    try:
        fs_upload_cmd = [
            env.subst("$PYTHONEXE"),
            "-m",
            "platformio",
            "run",
            "--target",
            "uploadfs",
            "--environment",
            env_name,
        ]
        print(f"Executing: {' '.join(fs_upload_cmd)}")
        subprocess.run(fs_upload_cmd, check=True, text=True, capture_output=False)
        print("STEP 2: Filesystem upload successful.")
    except subprocess.CalledProcessError as e:
        print(
            f"ERROR during filesystem upload step: Command exited with status {e.returncode}"
        )
        Exit(1)
    except Exception as e:
        print(f"ERROR during filesystem upload step: {e}")
        Exit(1)

    print("\n--- Custom Target: upload_all finished successfully ---")
    return None


# 注册自定义目标 "upload_all"
env.AddCustomTarget(
    name="upload_all",
    dependencies=None,  # <--- 添加这一行!
    actions=upload_all_action,
    title="Upload Firmware & Filesystem",
    description="Sequentially upload firmware and then the filesystem image",
)
