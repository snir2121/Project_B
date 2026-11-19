

<!-- Start of picture text -->
=<br>MW The Andrew and Erna Viterbi Faculty of THE: PROFS ISRAELI CEDERSAUM. ' TECH NION<br>MW Mew ELECTRICAL<br>Bees ENGINEERING& COMPUTER SYSTEMSHIGH SPEEDLABORATORY DIGITAL HsS DS< isa ntomiatvnI7 nenisv ntAaynn Israel Institute.<br>“M DIXIITY JAW" ‘sins w"v of Technology<br><!-- End of picture text -->

# Holter AI Analyzer Supervised by: Boaz Mizrachi Itamar Cohen – Noam Gouldman 

##### Background 

- Sudden Cardiac Death in young adults is often caused by inherited arrhythmias like Congenital Long QT and Brugada Syndromes. 

- The primary diagnostic tool is a continuous 24-hour 12-lead Holter monitor recording. 

- Current manual analysis is highly time-consuming, prone to human error, and requires expert electrophysiologists. 

- There is a critical need for an automated, AI-driven system to provide fast, reliable, and clinician-ready ECG analysis. 



<!-- Start of picture text -->
Thy 4 w<br>Wek i|<br>ER Va grenaa eas Fin fe A =<br>rr 4 le < (2——hh Z |<br><!-- End of picture text -->

#### Goals & Clinical Focus 

- Build an automated end-to-end pipeline for 24-hour 12lead Holter ECG analysis. 

- Accurately detect life-threatening Brugada (Type 1) and Long QT syndromes. 

- Utilize clinical guidance from Rambam Hospital to ensure diagnostic relevance. 

- Quantify "Disease Burden" via automated reporting for clinician review. 

- Research deep learning architectures for precise wave segmentation and timing. 



<!-- Start of picture text -->
OUTER—E56 FNAL REPORT<br>=<br><!-- End of picture text -->



<!-- Start of picture text -->
= 2<br>: Qe is= ae NN Do<br><!-- End of picture text -->



<!-- Start of picture text -->
4<br>4m<br><!-- End of picture text -->





###### Segmentation & Data Foundation 

- Trained on LUDB and ISP databases; validated on real-world Rambam hospital recordings. 

- Semantic segmentation classifies every signal point as P- wave, QRS complex, T-wave, or Background. 

- Enables precise automated extraction of clinical intervals and wave amplitudes. 

- Uses composite Dice and Weighted Cross-Entropy loss to handle >70% background imbalance. 

- Incorporates dV/dt derivatives as input channels to explicitly capture signal slopes. 

###### Architecture 

- Resamples signals to 128 Hz, 

   - applies bandpass/notch filtering, and performs Z-score normalization. Ae 

- Utilizes a 1D Attention U-Net encoder-decoder network to focus on precise wave boundaries. 

- Employs an ECG-SCFNet dualstream network to extract local high-frequency and global rhythmic patterns. 

- Combines both architectures into a weighted ensemble model for maximum morphological robustness. 

- Applies HR filters and local averaging during post-processing for precise QTc calculation. 

## Results 

- Achieved stable Dice scores exceeding 90% across all major ECG wave categories. 

- • Resolved a 15% cross-dataset performance drop by training on both datasets together. 

- • Validated model generalization using real-world ambulatory recordings from Rambam Hospital. 

- • Identified a consistent 30 ms clinical timing offset in automated Long QT interval measurements. 

- • Maintained high segmentation accuracy despite 

- significant muscle artifacts and baseline wander. 



- Quantifies daily disease burden to generate automated, clinicianready diagnostic reports. 

### Challenges and Future Work 

- Successfully developed an end-to-end pipeline that automatically converts raw ISHNE Holter files into comprehensive clinical risk reports. 

- • Proved that a combined training strategy effectively resolves the 15% domain shift, maintaining stable Dice scores above 90%. 

- • Demonstrated that wave timing precision is currently bound by a physical 128 Hz sampling rate quantization floor of 7.8 ms. 

- Constructed a robust data extraction and windowing infrastructure for Brugada patients to serve as a reliable foundation for future models. 

- • Future work will focus on analyzing original high-frequency hardware files to fully bypass the 128 Hz physical quantization ceiling. 

- Gathering broader clinical datasets will help validate the observed 30 ms measurement bias and fine-tune advanced post-processing filters. 

- • Next steps include extracting identical healthy control datasets to train a binary Brugada Syndrome classifier using the current segmentation architecture as a backbone. 

