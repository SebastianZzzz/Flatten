import os
import shutil
import readline
from pathlib import Path

def smart_flatten(source_dir):
    clean_dir = source_dir.strip().strip("'").strip('"')
    source_path = Path(clean_dir).expanduser().resolve()
    
    if not source_path.exists() or not source_path.is_dir():
        print(f"Error: 路径 '{source_path}' 不存在或不是文件夹！")
        return

    # --- 第一阶段：扫描 (Scanning) ---
    # 先把所有文件找出来，存入内存
    all_files = []
    for root, dirs, files in os.walk(source_path):
        for f in files:
            all_files.append(Path(root) / f)
    
    if not all_files:
        print("未发现任何文件。")
        return

    # --- 第二阶段：准备 (Preparation) ---
    # 在输入文件夹内部创建输出文件夹
    target_path = source_path / "FLATTENED_STASH" 
    target_path.mkdir(exist_ok=True)

    print(f"扫描完成，找到 {len(all_files)} 个文件。")
    print(f"目标目录: {target_path}")

    # --- 第三阶段：执行 (Execution) ---
    count = 0
    for file_path in all_files:
        # 重要：如果文件本身就在目标文件夹里，跳过，否则会无限循环搬运
        if target_path in file_path.parents:
            continue
            
        destination = target_path / file_path.name
        
        # 处理重名冲突
        if destination.exists():
            stem, suffix = file_path.stem, file_path.suffix
            counter = 1
            while destination.exists():
                destination = target_path / f"{stem}_{counter}{suffix}"
                counter += 1
        
        try:
            shutil.move(str(file_path), str(destination))
            count += 1
            print(f"[{count}] Moved: {file_path.name}")
        except Exception as e:
            print(f"Failed to move {file_path.name}: {e}")

    # --- 第四阶段：清理 (Cleanup) ---
    print("\n--- 正在清理空的原始子文件夹 ---")
    # 使用 topdown=False (后序遍历)，从最深层开始往上删
    for root, dirs, _ in os.walk(source_path, topdown=False):
        for name in dirs:
            dir_to_check = Path(root) / name
            
            if dir_to_check == target_path:
                continue
            
            try:
                os.rmdir(dir_to_check)
                print(f"Removed empty folder: {name}")
            except OSError:
                # 文件夹非空，直接跳过
                pass
    
    print(f"\n--- 任务完成 ---")
    print(f"成功压扁 {count} 个文件到: {target_path}")

if __name__ == "__main__":
    print("--- Auto-Naming Directory Flattener (Two-pass Edition) ---")
    raw_input = input("请拖入或输入要压扁的文件夹路径: ")
    smart_flatten(raw_input)