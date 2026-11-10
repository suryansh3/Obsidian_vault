"""
dip_pipeline.py
================
Digital Image Processing pipeline (GRAYSCALE ONLY) for tomato leaf
disease screening, restricted to four stages:

    1. Image Acquisition
    2. Sampling and Quantization
    3. Gray-Level Transformations
    4. Image Enhancement (Contrast Stretching + Histogram Equalization)

Input images :
    images/input/Tomato__healthy.JPG
    images/input/Tomato___Late_blight.JPG

Output figures (saved to images/output/) are referenced directly in the
report (report.md / report.tex).

Libraries: opencv-python, numpy, matplotlib, scikit-image
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# ---------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------
IN_DIR = os.path.join(os.path.dirname(__file__), "..", "images", "input")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images", "output")
os.makedirs(OUT_DIR, exist_ok=True)

HEALTHY_PATH = os.path.join(IN_DIR, "Tomato__healthy.JPG")
DISEASED_PATH = os.path.join(IN_DIR, "Tomato___Late_blight.JPG")


# =======================================================================
# SECTION 1 -- IMAGE ACQUISITION
# =======================================================================
def section1_acquisition():
    """Read both leaf images and load them directly as single-channel
    grayscale images. This is the acquisition stage: light reflected
    from the leaf is focused and sampled by the camera sensor into a
    discrete grid of pixel intensities f(x, y)."""

    gray_healthy = cv2.imread(HEALTHY_PATH, cv2.IMREAD_GRAYSCALE)
    gray_diseased = cv2.imread(DISEASED_PATH, cv2.IMREAD_GRAYSCALE)

    print("Healthy leaf  :", gray_healthy.shape, gray_healthy.dtype)
    print("Diseased leaf :", gray_diseased.shape, gray_diseased.dtype)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4.2))
    for ax, img, title in zip(
        axes, [gray_healthy, gray_diseased], ["Healthy leaf", "Late blight leaf"]
    ):
        ax.imshow(img, cmap="gray", vmin=0, vmax=255)
        ax.set_title(f"{title}\n{img.shape[0]}x{img.shape[1]}, 8-bit")
        ax.axis("off")
    fig.suptitle("Section 3.1 -- Image Acquisition (grayscale)")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "01_acquisition.png"), dpi=160)
    plt.close(fig)

    return gray_healthy, gray_diseased


# =======================================================================
# SECTION 2 -- SAMPLING AND QUANTIZATION
# =======================================================================
def subsample(img, factor):
    """Spatial sampling: keep every 'factor'-th pixel (reduces spatial
    resolution -> blocky / pixelated appearance)."""
    return img[::factor, ::factor]


def requantize(img, levels):
    """Amplitude quantization: collapse the 256 possible gray levels
    down to 'levels' levels (reduces gray-level resolution -> visible
    false contours / banding)."""
    factor = 256 // levels
    return (img // factor) * factor


def section2_sampling_quantization(gray_healthy, gray_diseased):
    sample_factors = [1, 4, 12, 24]
    quant_levels = [256, 16, 4, 2]

    for name, img in [("healthy", gray_healthy), ("diseased", gray_diseased)]:
        fig, axes = plt.subplots(2, 4, figsize=(12, 6.2))

        # Row 1: spatial sub-sampling
        for ax, f in zip(axes[0], sample_factors):
            sampled = subsample(img, f)
            ax.imshow(sampled, cmap="gray", vmin=0, vmax=255)
            ax.set_title(f"Sampled every {f}-th px\n({sampled.shape[0]}x{sampled.shape[1]})")
            ax.axis("off")

        # Row 2: amplitude re-quantization
        for ax, levels in zip(axes[1], quant_levels):
            requant = requantize(img, levels)
            ax.imshow(requant, cmap="gray", vmin=0, vmax=255)
            ax.set_title(f"{levels} gray levels")
            ax.axis("off")

        fig.suptitle(f"Section 3.2 -- Sampling (top) and Quantization (bottom): {name} leaf")
        fig.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"02_sampling_quantization_{name}.png"), dpi=160)
        plt.close(fig)


# =======================================================================
# SECTION 3 -- GRAY-LEVEL (INTENSITY) TRANSFORMATIONS
# =======================================================================
def section3_gray_level_transforms(gray_healthy, gray_diseased):
    for name, gray in [("healthy", gray_healthy), ("diseased", gray_diseased)]:
        gray_f = gray.astype(float) / 255.0

        negative = 255 - gray
        log_img = (np.log1p(gray_f) / np.log1p(1.0) * 255).astype("uint8")
        gamma_bright = (np.power(gray_f, 0.4) * 255).astype("uint8")   # gamma < 1: brighten
        gamma_dark = (np.power(gray_f, 2.5) * 255).astype("uint8")     # gamma > 1: darken

        images = [gray, negative, log_img, gamma_bright, gamma_dark]
        titles = ["Original", "Negative\ns=255-r", "Log transform\ns=c*log(1+r)",
                  "Power-law (gamma=0.4)\nbrighten", "Power-law (gamma=2.5)\ndarken"]

        fig, axes = plt.subplots(1, 5, figsize=(15, 3.4))
        for ax, im, t in zip(axes, images, titles):
            ax.imshow(im, cmap="gray", vmin=0, vmax=255)
            ax.set_title(t, fontsize=9)
            ax.axis("off")
        fig.suptitle(f"Section 3.3 -- Gray-Level Transformations: {name} leaf")
        fig.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"03_gray_level_transforms_{name}.png"), dpi=160)
        plt.close(fig)

        # transfer function curves s = T(r)
        r = np.linspace(0, 1, 256)
        s_negative = 1 - r
        s_log = np.log1p(r) / np.log1p(1.0)
        s_gamma_b = np.power(r, 0.4)
        s_gamma_d = np.power(r, 2.5)

        fig, ax = plt.subplots(figsize=(5.2, 5))
        ax.plot(r, r, "k--", label="Identity (no change)")
        ax.plot(r, s_negative, label="Negative")
        ax.plot(r, s_log, label="Log")
        ax.plot(r, s_gamma_b, label="Gamma = 0.4 (brighten)")
        ax.plot(r, s_gamma_d, label="Gamma = 2.5 (darken)")
        ax.set_xlabel("Input intensity r (normalized)")
        ax.set_ylabel("Output intensity s = T(r)")
        ax.set_title(f"Transfer functions used ({name} leaf)")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"03b_transform_curves_{name}.png"), dpi=160)
        plt.close(fig)


# =======================================================================
# SECTION 4 -- IMAGE ENHANCEMENT: CONTRAST STRETCHING + HISTOGRAM EQ.
# =======================================================================
def section4_enhancement(gray_healthy, gray_diseased):
    stats = {}

    for name, gray in [("healthy", gray_healthy), ("diseased", gray_diseased)]:
        # 1. Contrast stretching (2nd-98th percentile -> [0,255])
        p2, p98 = np.percentile(gray, (2, 98))
        stretched = exposure.rescale_intensity(gray, in_range=(p2, p98))

        # 2. Global histogram equalization
        equalized = cv2.equalizeHist(gray)

        fig, axes = plt.subplots(2, 3, figsize=(12, 7.4))

        # top row: images
        for ax, im, t in zip(
            axes[0],
            [gray, stretched, equalized],
            ["Original", f"Contrast-stretched\n(p2={p2:.0f}, p98={p98:.0f})", "Histogram-equalized"],
        ):
            ax.imshow(im, cmap="gray", vmin=0, vmax=255)
            ax.set_title(t, fontsize=9)
            ax.axis("off")

        # bottom row: histograms
        for ax, im, t, c in zip(
            axes[1],
            [gray, stretched, equalized],
            ["Original histogram", "Stretched histogram", "Equalized histogram"],
            ["gray", "tab:blue", "tab:red"],
        ):
            ax.hist(im.ravel(), bins=256, range=(0, 255), color=c, alpha=0.8)
            ax.set_title(t, fontsize=9)
            ax.set_xlabel("Gray level")
            ax.set_ylabel("Pixel count")
            ax.set_xlim(0, 255)

        fig.suptitle(f"Section 3.4 -- Contrast Stretching & Histogram Equalization: {name} leaf")
        fig.tight_layout()
        fig.savefig(os.path.join(OUT_DIR, f"04_enhancement_{name}.png"), dpi=160)
        plt.close(fig)

        stats[name] = {
            "mean": float(np.mean(gray)),
            "std": float(np.std(gray)),
            "p2": float(p2),
            "p98": float(p98),
            "dynamic_range": float(p98 - p2),
            "mean_stretched": float(np.mean(stretched)),
            "std_stretched": float(np.std(stretched)),
            "mean_equalized": float(np.mean(equalized)),
            "std_equalized": float(np.std(equalized)),
        }

    # Overlaid histogram comparison: healthy vs diseased (original grayscale)
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.hist(gray_healthy.ravel(), bins=256, range=(0, 255), color="tab:green",
            alpha=0.55, label="Healthy leaf")
    ax.hist(gray_diseased.ravel(), bins=256, range=(0, 255), color="tab:brown",
            alpha=0.55, label="Late blight leaf")
    ax.set_xlabel("Gray level")
    ax.set_ylabel("Pixel count")
    ax.set_title("Original grayscale histograms: healthy vs. diseased leaf")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "04b_histogram_comparison.png"), dpi=160)
    plt.close(fig)

    return stats


if __name__ == "__main__":
    gray_healthy, gray_diseased = section1_acquisition()
    section2_sampling_quantization(gray_healthy, gray_diseased)
    section3_gray_level_transforms(gray_healthy, gray_diseased)
    stats = section4_enhancement(gray_healthy, gray_diseased)

    print("\n--- Summary statistics (Section 3.4) ---")
    for name, s in stats.items():
        print(f"\n{name.upper()} LEAF")
        for k, v in s.items():
            print(f"  {k:18s}: {v:.2f}")
