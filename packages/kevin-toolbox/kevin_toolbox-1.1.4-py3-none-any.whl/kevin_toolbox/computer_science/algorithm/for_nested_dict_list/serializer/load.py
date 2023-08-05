import os
import torch
import torch
import numpy as np
from kevin_toolbox.computer_science.algorithm import for_nested_dict_list as fndl


def load(var, file_path, b_exclude_non_state_part_in_exp=True, **kwargs):
    """
        加载状态到 exp 中
            主要读取 file_path 的文件中以下两方面的状态信息：
                - exp 中实例的状态（只有具有 load_state_dict() 方法的实例才会加载状态）
                - torch 和 numpy 的随机生成器的状态
            file_path 的文件格式参见 save_state_to_file()

        参数：
            var:                    <nested dict list>
            settings:               <dict>
            b_exclude_non_state_part_in_exp:    <boolean> 是否不更新exp中非状态部分
                                                    默认为 True
    """
    print("Loading ...")
    assert os.path.isfile(file_path), f'file {file_path} not found!'

    state_s = torch.load(file_path)

    # for_exp
    for name, value in fndl.get_nodes(var=exp, level=-1, b_strict=True):
        try:
            v = fndl.get_value_by_name(var=state_s["for_exp"], name=name)
        except:
            print(f'failed to load state of {name}, because missing in the file')
            continue

        if callable(getattr(value, "load_state_dict", None)):
            value.load_state_dict(v)
        elif not b_exclude_non_state_part_in_exp:
            fndl.set_value_by_name(var=exp, name=name, value=v)

    # for_rng
    if "for_rng" in state_s:
        np.random.set_state(state_s["for_rng"]["numpy"])
        torch.set_rng_state(state_s["for_rng"]["torch"])
        if torch.cuda.is_available() and state_s["for_rng"]["torch_cuda"] is not None:
            torch.cuda.set_rng_state(state_s["for_rng"]["torch_cuda"])

    print(f'Loaded state from {file_path}')
    return state_s
