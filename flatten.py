import os
import shutil
import readline
from pathlib import Path

def flatten_directory(source_dir):
    # 1. 预处理路径：去掉首尾空格，并移除用户拖拽时可能带入的各种引号
    clean_src = source_dir.strip().strip("'").strip('"')
    source_path = Path(clean_src).expanduser().resolve()

    if not source_path.exists() or not source_path.is_dir():
        print(f"Error: 路径 '{source_path}' 不是有效的文件夹！")
        return

    # 2. 自动生成目标路径
    target_path = source_path.parent / f"{source_path.name}_flattened"

    if not target_path.exists():
        target_path.mkdir(parents=True)
        print(f"Created target directory: {target_path}")
    else:
        print(f"Using existing target directory: {target_path}")

    count = 0

    for root, dirs, files in os.walk(source_path):
        # 安全检查：防止死循环
        if os.path.abspath(root).startswith(os.path.abspath(target_path)):
            continue
            
        for filename in files:
            file_path = Path(root) / filename
            destination = target_path / filename
            
            # 3. 处理重名冲突
            if destination.exists():
                stem = destination.stem
                suffix = destination.suffix
                counter = 1
                while destination.exists():
                    destination = target_path / f"{stem}_{counter}{suffix}"
                    counter += 1
            
            try:
                shutil.move(str(file_path), str(destination))
                count += 1
                # 修复点：直接打印文件名字符串，不再调用 .name
                print(f"[{count}] Moved: {filename}")
            except Exception as e:
                print(f"Failed to move {filename}: {e}")

    print(f"\n--- 任务完成 ---")
    print(f"共处理文件: {count} 个")
    print(f"结果存放于: {target_path}")

if __name__ == "__main__":
    print("--- Auto-Naming Directory Flattener ---")
    # 获取输入后立即处理引号
    raw_input = input("请拖入或输入要压扁的文件夹路径: ")
    flatten_directory(raw_input)