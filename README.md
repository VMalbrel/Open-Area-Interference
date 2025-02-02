# Open-Area-Interference
Summary
Developed a machine learning image recognition model to analyze interference areas in perforated metal sheets at various angles. This model was used to determine acceptable helical angles for optimized manufacturing.
Optimized Video Capture for Open Area Calculation
To ensure accurate open area calculations, video files must be in uncompressed .AVI format, as compressed formats (e.g., MP4) significantly reduce accuracy. A minimum resolution of 3000x300 pixels is required, with the following recommended setups to maximize SolidWorks’ 4.00 GB file size limit:
1 FPS at 4500x4500 (preferred)
2 FPS at 3000x3000
The video capture area is optimized with a height and width of 5.00 inches, calculated based on 2 × radius × cos(45°). This maximizes perforation visibility while preventing plate offsets from affecting results.
To correct SolidWorks’ automatic cropping, the crop box is adjusted by reducing its index by 2 on all sides, a value determined experimentally. The final processed video undergoes binary brightness conversion, where 0 represents closed areas and 255 represents open areas.
For improved adaptability, crop box indexing should be set as a percentage of the total resolution.
