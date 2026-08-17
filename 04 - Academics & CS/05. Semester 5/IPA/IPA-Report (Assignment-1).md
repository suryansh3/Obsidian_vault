# Automated Detection of Late Blight Disease in Tomato Leaves Using Digital Image Processing

**A Course Project Report — Unit I: Introduction and Digital Image Fundamentals**

---

**Author:** _[Suryansh Mithu]_ **Course:** Image Processing and Analysis (IPA) **Date:** 17 August 2026

---

## Abstract

Plant diseases such as late blight cause enormous crop losses every year, and farmers often cannot tell early on whether a leaf is genuinely sick or just dusty or sun-stressed. This report builds a small, self-contained digital image processing (DIP) pipeline that takes a photograph of a tomato leaf and decides whether it is healthy or diseased, using nothing but classical image processing — no deep learning. We use real photographs from the public **PlantVillage dataset** and walk through every stage covered in Unit I of the course: image acquisition, sampling and quantization, gray-level transformations, histogram-based enhancement, image restoration, colour image processing, wavelet/multiresolution analysis, compression, morphological processing, segmentation, representation & description, and finally a simple rule-based recognition step. All code is written in Python using OpenCV, scikit-image, PyWavelets, NumPy and Matplotlib. On our two test images the pipeline correctly separates a **healthy leaf (0.0% lesion area)** from a **late-blight-infected leaf (33.0% lesion area)**.

---

## 1. Introduction and Problem Statement

### 1.1 Why this problem?

Tomato is one of the most widely grown vegetable crops in the world, and **late blight** (caused by the oomycete _Phytophthora infestans_) is one of its most destructive diseases — it was, famously, the cause of the Irish potato famine on the related potato crop. Late blight spreads quickly in humid weather and can destroy an entire field within days if it is not caught early. Smallholder farmers frequently do not have access to a plant pathologist and must decide, just by looking at a leaf, whether it needs treatment.

This project asks a simple, concrete question:

> **Given a photograph of a single tomato leaf, can a computer program — using only classical digital image processing techniques — automatically estimate how much of the leaf is diseased, and issue a simple diagnosis (healthy / mild / severe)?**

This is a _mid-level_ to _high-level_ image processing task in the vocabulary of Unit I: it starts from a raw image, moves through low-level pre-processing (denoising, contrast enhancement), continues into mid-level processing (segmentation, feature description), and ends with a high-level decision (recognition/classification).

### 1.2 Why classical DIP instead of deep learning?

Convolutional neural networks are the state of the art for this exact problem (the PlantVillage dataset is, in fact, the standard benchmark for CNN-based plant disease classifiers). However, the purpose of this report is to demonstrate the **fundamentals of digital image processing** taught in Unit I — sampling, quantization, gray-level transforms, histograms,— and to show that a surprisingly competent diagnostic tool can be built from these building blocks alone, with a transparent and explainable decision rule.

---

## 2. Dataset

We use the **PlantVillage Dataset**, a large, publicly available collection of over 50,000 labelled leaf images spanning 14 crop species and 38 disease/healthy classes, originally released to support the paper _"Using Deep Learning for Image-Based Plant Disease Detection"_ (Mohanty, Hughes & Salathé, 2016).

- **GitHub repository (images used in this report):** `https://github.com/spMohanty/PlantVillage-Dataset`
- **Original paper:** Mohanty, S.P., Hughes, D.P., Salathé, M. (2016). _Using Deep Learning for Image-Based Plant Disease Detection_, Frontiers in Plant Science. `https://arxiv.org/abs/1604.03169`
- **Kaggle mirror:** `https://www.kaggle.com/datasets/emmarex/plantdisease`

From this dataset we selected two greyscale images (256×256 pixels, RGB, JPEG) from the `raw/greyscale` split:

|Image|Class folder|Ground truth|
|---|---|---|
|`healthy_leaf.jpg`|`Tomato___healthy`|Healthy|
|`diseased_leaf.jpg`|`Tomato___Late_blight`|Late blight (diseased)|

Both images are shown in Figure 1 — this is the raw output of the **image acquisition** stage of the pipeline (Section 3.1).

![Figure 1: Acquired images](https://claude.ai/outputs/01_acquisition.png)

_Figure 1. The two leaf photographs used throughout this report, exactly as supplied by the sensor/camera and stored in the dataset._

---

## 3. Methodology — The Digital Image Processing Pipeline

Following Unit I of the course, we treat the diseased leaf image as the primary "patient" image and pass it through the following pipeline. Every stage below corresponds directly to a topic taught in the lecture slides. The full, runnable source code is given in Appendix A and is also provided as a standalone file, `dip_pipeline.py`.

### 3.1 Image Acquisition

An image is captured when a scene is illuminated, light reflects off the leaf, and a camera's sensor focuses and samples that light into a discrete grid of pixels. In our case, "acquisition" is simply reading the JPEG file that a smartphone camera already produced:

```python
import cv2
bgr = cv2.imread("diseased_leaf.jpg")
img_rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)   # OpenCV loads as BGR
print(img_rgb.shape)   # (256, 256, 3)  ->  M=256 rows, N=256 cols, 3 colour channels
```

The image is a function `f(x, y)` of two spatial coordinates, and because both the coordinates and the intensity values are finite and discrete, it is — by definition — already a **digital image**.

### 3.2 Sampling and Quantization

The lecture defines _sampling_ as digitizing the spatial coordinates and _quantization_ as digitizing the amplitude (gray level). To make this concept visible, we artificially re-sample and re-quantize the grayscale version of the leaf image:

```python
def subsample(img, factor):
    return img[::factor, ::factor]          # keep every k-th pixel

def requantize(img, levels):
    factor = 256 // levels
    return (img // factor) * factor          # collapse to L gray levels
```

Figure 2 shows what happens as we reduce the sampling rate (top row) and the number of quantization levels (bottom row). Coarser sampling produces a blocky, pixelated image (loss of spatial resolution), while coarser quantization produces visible "banding" or false contours (loss of gray-level resolution) — exactly the two effects described in the lecture.

![Figure 2: Sampling and quantization](https://claude.ai/outputs/02_sampling_quantization.png)

_Figure 2. Top row: the image sampled every 1st, 4th, 12th and 24th pixel. Bottom row: the same image quantized to 256, 16, 4 and 2 gray levels._

### 3.3 Gray-Level (Intensity) Transformations

Before doing anything complicated, Unit I teaches the three classical point-wise gray-level transformation functions `s = T(r)`:

- **Negative transform:** `s = 255 - r` (useful for highlighting dark detail in bright regions, similar to a photographic negative).
- **Log transform:** `s = c · log(1 + r)` (compresses the dynamic range, brings out low-intensity detail).
- **Power-law / gamma transform:** `s = c · r^γ` (γ < 1 brightens the image, γ > 1 darkens it — this is exactly what "gamma correction" on a monitor does).

```python
gray_f = gray.astype(float) / 255.0
negative = 255 - gray
log_img  = (np.log1p(gray_f) / np.log1p(1.0) * 255).astype("uint8")
gamma_img = (np.power(gray_f, 0.4) * 255).astype("uint8")   # brighten
```

![Figure 3: Gray-level transformations](https://claude.ai/outputs/03b_gray_level_transforms.png)

_Figure 3. From left to right: original, negative, log transform, and two power-law (gamma) transforms — one that brightens the leaf (γ = 0.4) and one that darkens it (γ = 2.5)._

![Figure 4: Transfer functions](https://claude.ai/outputs/03c_transform_curves.png)

_Figure 4. The actual `s = T(r)` curves used to produce Figure 3, plotted on normalised axes. The dashed line is the identity transform (no change)._

The log transform and the brightening gamma curve (γ = 0.4) are particularly useful here because the necrotic (dead, brown) part of the leaf is quite dark; stretching the dark end of the histogram makes its internal texture visible.

### 3.4 Image Enhancement (Contrast Stretching and Histogram Equalization)

Enhancement improves the _visual quality_ of the image for a human viewer or a downstream algorithm — it does not try to reconstruct a "true" image, it simply makes important details easier to see. We apply three enhancement techniques:

1. **Contrast stretching** — linearly re-scales intensities between the 2nd and 98th percentile of the histogram to [0, 255], removing outliers without a full histogram equalization.
2. **Global histogram equalization** — flattens the cumulative histogram so that all gray levels are used equally, maximising global contrast.
3. **CLAHE (Contrast-Limited Adaptive Histogram Equalization)** — performs histogram equalization in small local tiles, so that local contrast is enhanced without over-amplifying noise in flat regions (this is the colour version, applied on the V channel of HSV).

```python
p2, p98 = np.percentile(gray, (2, 98))
stretched = exposure.rescale_intensity(gray, in_range=(p2, p98))

equalized = cv2.equalizeHist(gray)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(gray)
```

![Figure 5: Enhancement](https://claude.ai/outputs/03_enhancement.png)

_Figure 5. Top row: colour enhancement via global histogram equalization and CLAHE. Bottom row: grayscale, contrast-stretched, and the histogram before (grey) and after (red) equalization — note how equalization spreads the histogram out to fill the whole [0,255] range._

### 3.5 Image Restoration

Enhancement is subjective ("make it look nicer"); **restoration** is objective — it tries to invert a _known or estimated_ degradation model,

```
g(x, y) = h(x, y) * f(x, y) + n(x, y)
```

where `f` is the true image, `h` is a blur/degradation function, `n` is noise, and `g` is what we actually observe. To demonstrate this, we artificially degrade the leaf image with Gaussian blur and additive Gaussian noise, and then try to recover it using (a) Wiener filtering — the classical, textbook restoration filter — and (b) Non-Local-Means denoising, a more modern edge-preserving alternative.

```python
blurred  = cv2.GaussianBlur(gray_f, (9, 9), sigmaX=3)
degraded = random_noise(blurred, mode="gaussian", var=0.004)

restored_wiener = restoration.wiener(degraded, np.ones((5, 5)) / 25, balance=0.02)
restored_nlm    = cv2.fastNlMeansDenoising((degraded*255).astype("uint8"), h=12)
```

![Figure 6: Restoration](https://claude.ai/outputs/04_restoration.png)

_Figure 6. Left to right: original, artificially degraded (blur + noise), Wiener-restored, and Non-Local-Means-denoised. NLM does a visibly better job of removing the speckle noise while keeping the leaf edges sharp._

We measure restoration quality with **PSNR (Peak Signal-to-Noise Ratio)** against the original image:

|Image|PSNR vs. original|
|---|---|
|Degraded (blur + noise)|22.0 dB|
|Restored (Non-Local-Means)|25.2 dB|

A higher PSNR means the restored image is closer to the original — the restoration recovered about 3.2 dB of signal quality.

### 3.6 Colour Image Processing

A colour photograph is a vector-valued function `P(x,y) = [R, G, B]`. Many image processing tasks become _easier_ if we first move to a different colour space. We convert the RGB leaf image to **HSV** (Hue-Saturation-Value, which separates colour from brightness) and to **CIELAB** (which separates lightness `L` from two opponent colour axes `a*` and `b*`). The `a*` channel, in particular, is very good at separating green healthy tissue from brown/red diseased tissue, so we also generate a **pseudocolour** map of it using a "jet" colour map — a classic DIP visualisation trick for highlighting subtle intensity differences that the human eye would otherwise miss in a grayscale image.

```python
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)
a_channel = lab[:, :, 1]
pseudocolor = cv2.applyColorMap(cv2.normalize(a_channel, None, 0, 255,
                                               cv2.NORM_MINMAX).astype("uint8"),
                                 cv2.COLORMAP_JET)
```

![Figure 7: Colour processing](https://claude.ai/outputs/05_colour_processing.png)

_Figure 7. Original RGB, the Hue channel, the LAB `a*` channel (diseased tissue appears noticeably brighter/different here than healthy tissue), and a pseudocolour rendering of that channel._

### 3.7 Wavelets and Multiresolution Processing

Wavelets let us look at an image simultaneously in space and in frequency, at multiple scales. A single-level 2-D Haar wavelet transform splits the image into four sub-bands:

- **LL** — a coarser, low-pass approximation of the image (the "big picture").
- **LH / HL** — horizontal and vertical edge/detail information.
- **HH** — diagonal detail (fine texture, noise).

```python
import pywt
LL, (LH, HL, HH) = pywt.dwt2(gray, "haar")
```

![Figure 8: Wavelet decomposition](https://claude.ai/outputs/06_wavelet_decomposition.png)

_Figure 8. Single-level Haar wavelet decomposition. The LL band is a half-resolution smoothed copy of the leaf; the three detail bands pick out the leaf's veins and lesion boundary as bright edges._

Repeating the decomposition on the LL band gives a **multiresolution pyramid** — this is the same idea used in JPEG2000 compression and in many noise-reduction and image-fusion algorithms.

![Figure 9: Multilevel wavelet decomposition](https://claude.ai/outputs/07_wavelet_multilevel.png)

_Figure 9. A 2-level Haar decomposition, arranged in the classic "pyramid-of-quadrants" layout._

### 3.8 Image Compression

Storing and transmitting images cheaply matters a lot in agricultural settings where farmers may be uploading photos over a slow mobile connection. We compare the **raw** (uncompressed) image size against **lossless PNG** and **lossy JPEG** compression at several quality levels:

```python
cv2.imwrite("out.png", gray)                                  # lossless
cv2.imwrite("out.jpg", gray, [cv2.IMWRITE_JPEG_QUALITY, 50])   # lossy, Q=50
```

|Encoding|File size|Compression ratio|PSNR vs. raw|
|---|---|---|---|
|Raw (uncompressed)|64.0 KB|1.0×|—|
|PNG (lossless)|40.4 KB|1.6×|∞ (exact)|
|JPEG Q = 90|14.9 KB|4.3×|46.9 dB|
|JPEG Q = 50|8.4 KB|7.7×|32.3 dB|
|JPEG Q = 20|3.3 KB|19.7×|30.4 dB|
|JPEG Q = 5|1.6 KB|39.9×|26.3 dB|

![Figure 10: Compression](https://claude.ai/outputs/08_compression.png)

_Figure 10. Visual quality versus file size trade-off. Even at Q = 20 the lesion boundary is still clearly visible, which means a farmer's app could safely use aggressive JPEG compression to save mobile data without hurting the diagnosis._

### 3.9 Image Segmentation

This is the most important stage for our problem: we need to separate the **leaf** from the **background**, and then separate the **diseased** (necrotic/brown) tissue from the **healthy** (green) tissue on the leaf.

We use a simple but effective **two-stage colour thresholding** approach in HSV space:

1. **Leaf vs. background:** the cardboard/soil background in these photos is desaturated (low Saturation), whereas plant tissue — healthy or diseased — is strongly saturated. Thresholding the **Saturation** channel (with Otsu's method) cleanly separates the leaf silhouette from the background.
2. **Lesion vs. healthy tissue:** within the leaf silhouette, healthy green tissue has a distinctly different **Hue** than brown/necrotic tissue. Thresholding the Hue channel isolates the diseased regions.

```python
hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)

leaf_mask = s > 50                       # Stage 1: leaf silhouette
lesion    = (h < 25) & leaf_mask         # Stage 2: necrotic tissue
```

Small speckles are removed and holes are filled using `skimage.morphology.remove_small_objects` / `remove_small_holes`, and we keep only the single largest connected leaf blob (to discard any stray green pixels from other leaves in the background).

![Figure 11: Segmentation](https://claude.ai/outputs/09_segmentation.png)

_Figure 11. From left to right: original image, the leaf silhouette mask (background removed), the final lesion mask, and the lesion boundary overlaid in red on the original photo. The segmentation closely follows the visible brown necrotic patch._

### 3.10 Morphological Processing

Raw thresholded masks are usually noisy — they have small holes, ragged edges, and stray specks. Morphological operators, built from a small **structuring element** (we use a disk of radius 2), clean this up:

- **Erosion** shrinks the mask and removes small bright specks.
- **Dilation** grows the mask and fills small gaps.
- **Opening** (erosion → dilation) removes small isolated noise blobs while preserving the overall shape.
- **Closing** (dilation → erosion) fills small holes inside the lesion region.

```python
from skimage import morphology
se = morphology.disk(2)
opened = morphology.opening(lesion_mask, se)
closed = morphology.closing(lesion_mask, se)
```

![Figure 12: Morphological processing](https://claude.ai/outputs/10_morphology.png)

_Figure 12. Effect of erosion, dilation, opening and closing on the raw lesion mask. Opening cleans up small speckle noise; closing fills the small gaps inside the lesion._

### 3.11 Representation and Description

Once the lesion is segmented, we label each **connected component** (individual lesion patch) and describe it with a small feature vector: **area**, **perimeter**, **eccentricity** (how elongated the patch is), **circularity** `4πA/P²` (1.0 = perfect circle), and **mean intensity**.

```python
from skimage import measure
labeled = measure.label(lesion_mask, connectivity=2)
for region in measure.regionprops(labeled, intensity_image=gray):
    print(region.area, region.perimeter, region.eccentricity)
```

![Figure 13: Representation and description](https://claude.ai/outputs/11_representation_description.png)

_Figure 13. Left: bounding boxes around each individually detected lesion region. Right: the numeric feature table (label, area, perimeter, eccentricity, circularity, mean intensity) extracted for each region — this is exactly the kind of feature vector a classifier (rule-based or learning-based) would use downstream._

Our pipeline detected **5 separate necrotic regions** on the diseased leaf, the largest of which corresponds to the big blighted patch visible in the centre of the leaf.

### 3.12 Object Recognition (Diagnosis)

Finally, we close the loop with a simple **rule-based classifier** — the "high-level" stage of the pipeline, in the language of Unit I, where the input is attributes (from Section 3.11) and the output is a decision. We use one interpretable feature, the **percentage of leaf area that is diseased**, and apply simple thresholds:

```python
pct_diseased = 100 * lesion_area / leaf_area
if pct_diseased < 2:
    diagnosis = "HEALTHY"
elif pct_diseased < 12:
    diagnosis = "EARLY-STAGE / MILD INFECTION"
else:
    diagnosis = "SEVERE LATE BLIGHT INFECTION"
```

![Figure 14: Final diagnosis](https://claude.ai/outputs/12_object_recognition.png)

_Figure 14. Final output of the complete pipeline on both test images._

---

## 4. Results Summary

|Image|Leaf area (px)|Lesion area (px)|% Diseased|Diagnosis|Ground truth|
|---|---|---|---|---|---|
|`healthy_leaf.jpg`|27,918|0|0.0%|HEALTHY|Healthy ✅|
|`diseased_leaf.jpg`|30,636|10,105|33.0%|SEVERE LATE BLIGHT|Late blight ✅|

The pipeline correctly diagnoses both test images using **only classical image-processing techniques** — no machine learning model was trained. This matches the ground-truth folder labels from the PlantVillage dataset and demonstrates that a carefully engineered classical pipeline can still solve a meaningful real-world problem.

---

## 5. Discussion and Limitations

- **Threshold sensitivity.** The Hue/Saturation thresholds (`s > 50`, `h < 25`) were tuned by inspecting the pixel statistics of just two images. A production system would need thresholds validated across hundreds of images taken under different lighting conditions, or an adaptive method such as Otsu's algorithm applied per-image.
- **Confounding factors.** Shadows, senescence (natural leaf ageing/yellowing) and soil splashes can all lower the "greenness" of a leaf and could be mistaken for disease by a purely colour-based rule. A more robust system would combine colour features with **texture features** (e.g. from the wavelet detail bands in Section 3.7, or gray-level co-occurrence matrices) to reduce false positives.
- **Single-leaf assumption.** Our leaf-vs-background segmentation (Section 3.9) keeps only the single largest connected component, so it would fail on images containing several separate, non-touching leaves.
- **Why this still matters.** Despite these limitations, this project shows that image acquisition → enhancement → restoration → colour processing → wavelet analysis → compression → segmentation → morphology → representation → recognition is not just an abstract syllabus outline — it is a genuinely usable recipe for building a real (if simple) computer-vision application, and every stage is fully transparent and explainable, unlike a black-box neural network.

---

## 6. Conclusion

We built a complete, end-to-end digital image processing pipeline, following every stage taught in Unit I of the course, to solve a real agricultural problem: automatically detecting late blight disease on tomato leaves from a photograph. Using real images from the public PlantVillage dataset and standard Python libraries (OpenCV, scikit-image, PyWavelets, NumPy, Matplotlib), the pipeline successfully and correctly distinguished a healthy leaf from a severely diseased one, and produced an interpretable, human- readable diagnosis together with quantitative shape/colour descriptors for every detected lesion. This confirms that the fundamental DIP concepts — sampling and quantization, gray-level transformations, histogram-based enhancement, restoration, colour spaces, wavelets, compression, morphology, segmentation, representation/description, and recognition — fit together into a coherent and practically useful pipeline.

---

## References

1. Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016). _Using Deep Learning for Image-Based Plant Disease Detection._ Frontiers in Plant Science, 7, 1419. `https://arxiv.org/abs/1604.03169`
2. PlantVillage Dataset (GitHub mirror): `https://github.com/spMohanty/PlantVillage-Dataset`
3. PlantVillage Dataset (Kaggle mirror): `https://www.kaggle.com/datasets/emmarex/plantdisease`
4. Gonzalez, R. C., & Woods, R. E. _Digital Image Processing_ (4th ed.). Pearson — course textbook for Unit I concepts (image formation, sampling/quantization, gray-level transforms, enhancement, restoration, colour, wavelets, compression, morphology, segmentation, representation, recognition).
5. OpenCV documentation: `https://docs.opencv.org`
6. scikit-image documentation: `https://scikit-image.org`
7. PyWavelets documentation: `https://pywavelets.readthedocs.io`

---

## Appendix A — Full Python Source Code

The complete, runnable pipeline (`dip_pipeline.py`) used to generate every figure and table in this report is included alongside this document. Key library versions used: `opencv-python 4.13`, `scikit-image 0.26`, `PyWavelets 1.9`, `numpy 2.4`, `matplotlib 3.10`.

```python
# See dip_pipeline.py for the full, runnable script.
# It is organised into the same 12 numbered sections as this report:
#   1. Image Acquisition
#   2. Sampling & Quantization
#   3. Gray-Level Transformations + Enhancement (contrast stretch, histogram eq., CLAHE)
#   4. Image Restoration (Wiener filter, Non-Local-Means denoising)
#   5. Colour Image Processing (HSV, LAB, pseudocolour)
#   6. Wavelets & Multiresolution Processing (Haar DWT, 2-level pyramid)
#   7. Image Compression (PNG vs JPEG at multiple quality levels)
#   8. Image Segmentation (Saturation + Hue thresholding)
#   9. Morphological Processing (erosion, dilation, opening, closing)
#  10. Representation & Description (region features)
#  11. Object Recognition (rule-based diagnosis)
```