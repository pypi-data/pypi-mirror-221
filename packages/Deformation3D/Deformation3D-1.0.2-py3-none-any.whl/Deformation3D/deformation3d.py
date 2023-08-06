import os.path
import sys, os

from Deformation3D.generate_vox import generate_one
from Deformation3D.obj_2_points import restore_one_point_cloud, clear_pcd

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import deform

def hello():
    print("hello")


def prepare_vega_files(txt_filepath, vega_dir, leaf_num, voxel_size=0.02, normal=True):
    """
    变形前文件准备
    :param txt_filepath: 点云文件路径： /home/xxx/datasets/pcd/1.txt
    :param vega_dir: 生成vega文件的目录:  /home/xxx/datasets/vega/
    :param voxel_size:
    :param normal:
    :return:
    """
    os.makedirs(vega_dir, exist_ok=True)
    txt_filepath_split = os.path.split(txt_filepath)
    data_root = txt_filepath_split[0]
    model_name = txt_filepath_split[1]
    generate_one(data_root, vega_dir, model_name, leaf_num, voxel_size=voxel_size, normal=normal)


def deform_models(config_filepath, txt_filepath, vega_dir, out_dir, leaf_num, new_num,
                  min_base_force, max_base_force, integrator_times=20):
    """
    :param config_filepath: 配置文件目录 configs/corn_vox.configs
    :param txt_filepath: 点云文件路径： /home/xxx/datasets/pcd/1.txt
    :param vega_dir: vega文件 /home/xxx/datasets/vega/
    :param out_dir: 生成 element vertices 的目录： /home/xxx/datasets/new_models_tmp/
    :param leaf_num: 叶子数量
    :param new_num: 生成新模型的数量
    :param min_base_force:  每个叶子上力的最小值
    :param max_base_force: 每个叶子上力的最大值
    :param integrator_times:  积分次数
    :return:
    """
    out_obj_dir = os.path.join(out_dir, "obj/")
    os.makedirs(out_obj_dir, exist_ok=True)
    model_name = os.path.split(txt_filepath)[1][:-4]
    deform.deform_run(config_filepath, vega_dir, out_obj_dir, model_name, leaf_num, new_num,
                      integrator_times, min_base_force, max_base_force)


def remove_dir(dir):
    if not os.listdir(dir):
        try:
            # 使用 os.rmdir() 删除空文件夹
            os.rmdir(dir)
            print(f"空文件夹 {dir} 已成功删除。")
        except OSError as e:
            print(f"删除文件夹 {dir} 时出现错误：{e}")

def get_models_pcd(out_dir, vega_dir, transform_axis=True, normal=False):
    """
    从模型中恢复点云数据
    :param out_dir:
    :param vega_dir: vega文件 /home/xxx/datasets/vega/
    :param transform_axis:
    :param normal:
    :return:
    """
    out_obj_dir = os.path.join(out_dir, "obj")
    out_src_dir = os.path.join(out_dir, "src")
    out_data_dir = os.path.join(out_dir, "data")
    os.makedirs(out_src_dir, exist_ok=True)
    os.makedirs(out_data_dir, exist_ok=True)

    for one_item in os.listdir(out_obj_dir):
        item_obj_dir = os.path.join(out_obj_dir, one_item)
        for one_vertices in os.listdir(item_obj_dir):
            if one_vertices[-12:-4] == "vertices":
                txt_name = one_vertices[:-13]
                try:
                    # 恢复点云数据
                    restore_one_point_cloud(item_obj_dir, vega_dir, out_src_dir, txt_name)
                    # 删除 vertices、elements
                    os.remove(os.path.join(item_obj_dir, f"{txt_name}_vertices.txt"))
                    os.remove(os.path.join(item_obj_dir, f"{txt_name}_elements.txt"))
                    # 去除异常数据
                    clear_pcd(out_src_dir, out_data_dir, f"{txt_name}.txt",
                              remove_outlier=True, transform_axis=transform_axis, normal=normal)
                    os.remove(os.path.join(out_src_dir, f"{txt_name}.txt"))
                except FileNotFoundError:
                    print("文件不存在，无法删除。")
                except OSError as e:
                    print(f"删除文件时出现错误：{e}")
                except:
                    print("其他错误")

        # 删除文件夹
        remove_dir(item_obj_dir)
    remove_dir(out_obj_dir)
    remove_dir(out_src_dir)
