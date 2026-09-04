  ## Detailed Architectural Breakdown

  ### 1. Offline Scientific ETL & Quantization Pipeline (tools/)

  • Technology: Python 3, NumPy, NetCDF4, Gzip
  • Architectural Role: Upstream ocean datasets (NOAA WOA23, NCEP GODAS, NASA MODIS, ESA OC-CCI) are tens of gigabytes, un-regridded, and lack CORS
  support for direct browser consumption.
  • Mechanism:
      • Standardizes spatial resolution to a


         ∘
    0.125

  bathymetry grid (592 × 464) and

       ∘
    1.0

  3D fields (74 × 58 × 35 levels across 13 monthly blocks).

  • Implements varuna.grid.v3 int8 block-quantization, slashing multi-gigabyte netCDF payloads down to 4.94 MB per year (*.i8.bin.gz) with negligible
  precision loss (

          ∘
    <0.036  C

  temperature, <0.030  PSU salinity).
  ──────
  ### 2. Edge-Native Serverless & 3-Tier Sync Backend (src/)

  • Technology: Hono Web Framework, TypeScript, Cloudflare Pages & Edge Workers
  • Architectural Role: Acts as an ultra-fast, zero-maintenance edge gateway and live observation proxy.
  • Key Patterns:
      • 3-Tier Sync Strategy for Live Feeds:
          1. T₀ (Static Snapshot): Shipped observations.json boots the full 400+ platform fleet with 0ms latency on cold start.
          2. T₁ (Edge Cache): Cloudflare Cache API serves warm requests in under 10  ms (15-min TTL).
          3. T₂ (Stale-While-Revalidate): Background asynchronous updates via executionCtx.waitUntil() fetch live Ifremer Argo and NOAA GTS feeds without
          blocking the user.
      • Decoupled API Contracts: Implements CF-1.8 and ERDDAP-compliant schemas (/api/capabilities, /api/point, /api/section, /api/area-stats). INCOIS
      can swap the storage backend with their production THREDDS/OPeNDAP servers without modifying the frontend.
      • Security Gateway: Telegram bot credentials (TELEGRAM_BOT_TOKEN) stay strictly server-side on the edge worker.

  ──────
  ### 3. Client Ingestion & Stream Processing (grid-core.js, ocean-model.js)

  • Technology: Browser Streams API (DecompressionStream), TypedArrays (Float32Array, Int8Array)
  • Architectural Role: Enables zero-bundle, high-speed asynchronous data hydration directly on the client.
  • Key Patterns:
      • In-Memory Streaming: Native browser multi-threaded decompression unpacks .i8.bin.gz files directly into TypedArrays without blocking the UI.
      • Time Machine Multi-Decadal Cache: Decoded year packs (1998–2025) are cached in memory with smart prefetching for instant temporal scrubbing.
      • Honest Time Semantics: Separates historical analysis from real-time and seasonal outlooks, preventing observation extrapolation beyond the
      current date.

  ──────
  ### 4. GPU Volumetric Rendering & Graphics Engine (scene.js, fields.js, particles.js, markers.js)

  • Technology: Three.js (v0.160.1 via native ES Modules importmap) + Custom GLSL Shaders
  • Architectural Role: Renders complex 4D ocean physics and massive observation fleets at a locked 60 FPS.
  • Key Patterns:
      • Dual-Grid Bathymetric Architecture:
          • Display Grid: 480 × 376 displaced mesh with tanh peak compression and separable Gaussian filtering for photorealistic visual shading.
          • Raw Science Grid: 592 × 464 int16 ETOPO elevation grid driving analytical point probes, coastline masking, and bathymetric cross-sections.
      • GPU-Accelerated Scalar Sampling: 4D ocean atlases are uploaded as 2D float texture sheets (NZ × NX by Months × NY). Custom GLSL fragment shaders
      perform real-time trilinear interpolation, depth slicing, volumetric raymarching, and bio-optical chlorophyll depth projection (Uitz et al. 2006
      LUT).
      • O(1) Single-Draw-Call Fleet Engine: The entire active fleet (390+ Argo floats, Gliders, RAMA moorings, CTD casts) renders as a single GPU Points
      draw call with Signed Distance Field (SDF) antialiased glyphs. Pointer proximity triggers a smooth 3D miniature model reveal via InstancedMesh with
      zero CPU raycasting.
      • Current Dynamics Suite: Tapered ribbon particles, RK2 (Runge-Kutta 2nd Order) streamlines, and 2D dart vectors advected directly in the GODAS
      vector field to show phenomena like the Somali Jet reversal.

  ──────
  ### 5. Prognostic Edge Intelligence & Advisory Engine (predict.js, hazard.js, advisory.js)

  • Technology: Pure Mathematical / Statistical Client-Side Inference Engines + Custom Canvas2D (charts.js)
  • Architectural Role: Transforms raw numerical fields into actionable operational and disaster forecasts directly in the browser without server
  roundtrips.
  • Key Patterns:
      • Ocean Genesis Potential (OGP): Combines Tropical Cyclone Heat Potential (TCHP = ρcₚ∫(T - 26)dz), D₂₆ isotherm depth, and SST, calibrated against
      30 years of IBTrACS data (176 genesis events, 1995–2024).
      • VARUNA-CLIPER & SHIPS-lite Forecast Models: Integrates +120h cyclone track, intensity, landfall cone, and shelf storm-surge estimates.
      • Operational Advisories & Telegram Relay: Automatically generates plain-language marine bulletins and relays real-time alerts to coastal teams via
      @varuna1_bot with local storage deduplication.

  ──────
  ### 💡 Summary of Architectural Highlights to Emphasize to Judges:

  1. Zero-Bundle Web-Standard Stack: No Webpack/Rollup build lock-in — pure ES Modules and CDN importmaps.
  2. Extreme Compression: 75% payload reduction (19.5  MB → 4.94  MB/year) via varuna.grid.v3 int8 quantization.
  3. GPU-First Offloading: Scalar interpolation, volumetric rendering, and fleet markers executed directly on the GPU.
  4. Resilient 3-Tier Edge Architecture: Instant T₀ offline boot with background T₁/T₂ live synchronization.
  5. Standards-Compliant: ERDDAP and CF-1.8 REST API compatibility for instant INCOIS production readiness.