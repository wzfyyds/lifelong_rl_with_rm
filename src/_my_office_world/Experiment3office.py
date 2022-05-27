'''
Examine the effect of LLRM model in MineCraft
'''
import numpy as np

from src._my_lifelong import *
from src._my_plot_assistant import *

if __name__ == '__main__':
    from worlds.office_world import *
    import matplotlib.pyplot as plt

    is_plot = False
    if is_plot:
        plot_lifelong(title="Experiment3",
                      data_name="E3",
                      alg_list=["QRM", "QRMrs", "TQRM", "TQRMrs"],
                      plot_task_index=[i for i in range(3)],
                      to_steps=True,
                      save_fig=False,
                      use_normalize=True)
    else:
        param = OfficeWorldParams()
        office_env = OfficeWorld(param)
        A = ('until', ('not', 'n'), 'a')
        B = ('until', ('not', 'n'), 'b')
        C = ('until', ('not', 'n'), 'c')
        D = ('until', ('not', 'n'), 'd')
        c = ('until', ('not', 'n'), 'f')
        m = ('until', ('not', 'n'), 'e')
        o = ('until', ('not', 'n'), 'g')
        # tasks = [[('then', c, A), ('then', m, B)],
        #          [('then', c, o), ('then', m, o)],
        #          [('and', ('then', c, o), ('then', m, o)), ('then', B, A)],
        #          ]
        tasks = [[('then', c, A), ('then', m, B)],
                 [('then', c, o), ('then', m, o)],
                 [('then', ('and', c, m), o), ('then', B, A)],
                 ]
        steps_num = 30000
        repeated_test_times = 20
        propositions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        label_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '']
        gamma = 0.9
        alpha = 1.0
        epsilon = 0.1
        max_episode_length = 200
        save_data = True
        data_name = "E3"
        for algorithm in ["QRM", "QRMrs", "TQRM", "TQRMrs"]:
            run_lifelong(tasks,
                         steps_num=steps_num,
                         repeated_test_times=repeated_test_times,
                         env=office_env,
                         propositions=propositions,
                         label_set=label_set,
                         gamma=gamma,
                         alpha=alpha,
                         epsilon=epsilon,
                         max_episode_length=max_episode_length,
                         algorithm=algorithm,
                         save_data=save_data,
                         data_name=data_name)
