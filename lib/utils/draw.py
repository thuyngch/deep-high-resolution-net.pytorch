#------------------------------------------------------------------------------
#  Libraries
#------------------------------------------------------------------------------
import cv2
import numpy as np


#------------------------------------------------------------------------------
#  _COLORS
#------------------------------------------------------------------------------
_COLORS = [
	(255,255,255),
	(255,0,0),
	(0,255,0),
	(0,0,255),
	(255,255,0),
	(0,255,255),
	(255,0,255),
	(192,192,192),
	(128,128,128),
	(128,0,0),
	(128,128,0),
	(0,128,0),
	(128,0,128),
	(0,128,128),
	(0,0,128),
	(250,128,114),
	(85,107,47),
	(0,139,139),
	(147,112,219),
	(255,248,220),
]


#------------------------------------------------------------------------------
#  draw_heatmaps
#------------------------------------------------------------------------------
def draw_heatmaps(image, heatmaps):
	"""
	image (np.uint8) shape [H,W,3] with RGB format
	heatmaps (np.float32) shape [h,w,N] in range [0,1]
	"""
	# Resize heatmaps to image
	H, W = image.shape[:2]
	heatmaps = (255.0 * heatmaps).astype('uint8')
	heatmaps = cv2.resize(heatmaps, (W,H), interpolation=cv2.INTER_LINEAR)
	heatmaps = heatmaps.transpose((2,0,1))

	# Overlay
	_image = image.copy()
	overlay = np.zeros_like(_image)
	for idx, heatmap in enumerate(heatmaps):
		overlay[heatmap>0, :] = _COLORS[idx]
	overlaid_image = cv2.add(image, overlay)
	return overlaid_image
