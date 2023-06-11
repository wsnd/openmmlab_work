_base_ = [
    '_base_/models/resnet50.py', '_base_/datasets/fruit30_bs32.py',
    '_base_/schedules/fruit30_bs256_epochstep.py', '_base_/default_runtime.py'
]
