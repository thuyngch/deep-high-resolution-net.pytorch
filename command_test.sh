python tools/test.py \
	--cfg experiments/coco/hrnet/w32_256x192_adam_lr1e-3.yaml \
	TEST.MODEL_FILE /home/cybercore/thuync/checkpoints/HRNet/pose_coco/pose_hrnet_w32_256x192.pth \
	TEST.USE_GT_BBOX False
