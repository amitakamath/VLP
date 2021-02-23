#!/bin/bash
for MODEL_NO in {1..30};
  do
  echo ${MODEL_NO}
  python vlp/decode_img2txt.py --model_recover_path /home/amitak/VLP/checkpoints/trial/model.${MODEL_NO}.bin --new_segment_ids --batch_size 100 --beam_size 1 --enable_butd --image_root /home/amitak/VLP/data/COCO/region_feat_gvd_wo_bgd/ --split val --src_file /home/amitak/VLP/data/COCO/annotations/dataset_coco.json --file_valid_jpgs /home/amitak/VLP/data/COCO/annotations/coco_valid_jpgs.json
  echo
  echo
done
