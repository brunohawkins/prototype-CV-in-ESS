# Computer vision in endoscopic spinal surgery (CV in ESS)

Real-time surgical tool detection and tissue segmentation for endoscopic spinal surgery (ESS), built during a UCL Institute of Healthcare Engineering summer studentship (2024) with the Royal National Orthopaedic Hospital.

ESS causes less tissue trauma than open surgery, but its steep learning curve limits adoption in the UK. This project explores whether computer vision can help surgeons recognise anatomy and instruments in real time.

## What this repository contains

| Folder | Contents |
| --- | --- |
| [`preprocess/`](preprocess) | Data pipeline: join raw ESS clips, extract frames at 1 fps, split LabelMe annotations into boxes (tools) and polygons (anatomy), centre-crop and resize, clean labels, split into train/val/test, convert to YOLOv8 format |
| [`detection/`](detection) | `track_video.py`: runs the trained YOLOv8 detector with object tracking over a surgery video |
| [`preprocess/archive/`](preprocess/archive) | Earlier experiments not used in the final pipeline (TFRecord, XML/CSV conversion) |

The tissue segmentation code is hosted in Ziqi Zhang's repository: [IHE-summer-studentship-Endoscopic-Spinal-Surgery](https://github.com/King-in-black/IHE-summer-studentship-Endoscopic-Spinal-Surgery).

No patient data, video, annotations or trained weights are included.

## Results (prototype)

| Model | Task | Result | Speed |
| --- | --- | --- | --- |
| YOLOv8 | Tool detection (radiofrequency probe) | Recall 0.982, weighted F1 0.985 | 25-75 ms per frame on an M1 MacBook Pro |
| U-Net with attention | Tissue segmentation (6 classes: ligament, epidural fat, nerve, disc, working channel, background) | mIoU 69.4% | 30-50 ms per frame on an RTX 3060 |

- Data: one ~75-minute procedure split into six surgical phases, frames extracted at 1 fps, about 1,000 frames annotated in LabelMe with UCL fourth-year medical students.
- Only the radiofrequency probe had enough labelled examples for the detection prototype; other instruments need more data.
- Edge deployment on the Google Coral TPU is planned future work.

## Run the detector

```bash
pip install -r requirements.txt
python detection/track_video.py --weights path/to/best.pt --video path/to/video.mp4
```

## Outputs

- Abstract and poster, BioMedEng2024 (Queen Mary University of London, September 2024)
- Presentation, IDEAL 2024
- Published abstract in *BMJ Surgery, Interventions and Health Technologies*

## Team

Bruno Hawkins and Ziqi Zhang (tool detection and tissue segmentation, developed jointly), with Peter Snow, Daniel Yordanov, Michael Mokauem, Rui C. V. Loureiro and David Baxter (Aspire CREATe, UCL; Royal National Orthopaedic Hospital).
