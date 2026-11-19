

<!-- Start of picture text -->
HEE The Andrew and Erna Viterbi Faculty of<br>Mi Mee ELECTRICAL & COMPUTER<br>PTL ENGINEERING<br><!-- End of picture text -->



<!-- Start of picture text -->
rere | |. A<br>Bae 4S ost Fea<br>1A ene<br><!-- End of picture text -->



<!-- Start of picture text -->
os<br>V, TECHNION<br>AVE isract institute<br>of Technology<br><!-- End of picture text -->

Final Presentation Holter AI Analyzer 

**Students:** Noam Gouldman And Itamar Cohen **Supervisor:** Boaz Mizrachi **Semester:** Winter,  2026 **Date:** 23.06.2026 



<!-- Start of picture text -->
ESS 5s os. EES<br><!-- End of picture text -->

# Motivation 

- **Existing Problem:** Holter ECG analysis is manual, errorprone, and requires expert interpretation 

- • **Why It Matters:** Early and accurate detection of arrhythmias is critical for patient safety 



<!-- Start of picture text -->
| ————— 7 \@<br>tf INN ><br>SS ew—allZA<br>Zo 2TEN A<br><!-- End of picture text -->

- **Proposed Approach for Solution:** An automated AI-based system for fast, reliable Holter ECG analysis 



<!-- Start of picture text -->
Eas0S. Ee<br><!-- End of picture text -->

# Goal 

#### Develop a system that analyzes Holter ECG recordings by: 

- Recording multi-lead ECG signals over 24 hours 

- Processing and filtering the raw ECG data 

- Detecting arrhythmias using AI-based analysis 

- Generating a clear, clinician-ready diagnostic report 



<!-- Start of picture text -->
( A 1<br>EAN<br>EET aN<br><!-- End of picture text -->





<!-- Start of picture text -->
A 0 2 eae<br>cme °° aa<br>ME oo,  —<br><!-- End of picture text -->





<!-- Start of picture text -->
ewww TE<br>Een<br><!-- End of picture text -->



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Our Project Scope 

We are implementing the machine learning research phase including: 

- Understanding the physical and medical problem 

- • Exploring the data space and relevant signal heuristics • Researching ML methods for Holter ECG analysis • Creating a unified data lake for future development • Performing feature selection and methodology comparison 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Clinical Focus 

**The Challenge:** Sudden Cardiac Death in young adults (<35) is often caused by inherited arrhythmias. **The Problem:** These pathologies can be transient and are difficult to detect in standard manual analysis. **Our Solution Focus:** Following clinical guidance from Rambam Health Care Campus, our system targets two specific life-threatening conditions: 

- **Brugada Syndrome** (Type 1). 

- **Congenital Long QT Syndrome** . 



<!-- Start of picture text -->
Fees05. Ae<br><!-- End of picture text -->



<!-- Start of picture text -->
ECG Signal Analysis<br>a Sa a a a A aC | a a CP Ce<br>Le er aa ee er ee<br>BRR RRRPee<br>Bees eRe<br>BRAS RERSaae) (eee<br>SRA R SA eee<br>PpBERRREESER {TP PrN IeeeENa. SeeTT<br>PTT TTT TTT TW EE<br>FLT TT TTT TT te Tt tT | fi peate TT<br>feeSERRETed awl Pic Vie oadeeefie Fo Dl] ee<br><!-- End of picture text -->

Anatomy of a Heartbeat 



<!-- Start of picture text -->
asRE<br><!-- End of picture text -->

# Brugada Syndrome (Type 1) 

**Clinical Focus:** We target Type 1 identified by Dr. Blich as the only definitive diagnostic form. **Key Locations:** The pathology is primarily observed in V1, V2, V3 leads, or V5, V6 high leads. **The Detection Rule:** • Morphology Shape: A distinct "coved type" STsegment elevation • Threshold: Elevation of ≥ 2mm (0.2mV) at the J-point. 

**Normal ECG** 



<!-- Start of picture text -->
J point<br>Qa |<br>s<br><!-- End of picture text -->



<!-- Start of picture text -->
BRUGADA(V1/V2)TYPE1<br>Po ST Elevation<br>: > 2mm<br>(0.2mV)<br><!-- End of picture text -->



<!-- Start of picture text -->
EEEas os: EERE<br><!-- End of picture text -->

# Brugada Syndrome (Type 1) 



<!-- Start of picture text -->
Type 1 Type2 Types 4 Normal<br>vi ee oe a Vv<br>oe incee ae PEE agape<br>Hee: beep EEG<br>nda FOL egg R| V2 Ri +<br>V2 HPS! cheer cas T LA<br>EES iaa oe eo<br>othe eee = IpPree s 's<br>a tle Led} Vv<br>|<br>va eee ve ain ap 4 Ln<br>aun eae : paane HEE |g<br>wile HU HU | ws |<br>ve GEMEEREEangeeae EarMyo HaeEULA | V6 |<br>i ig sl Seer) 9 ~J| ~~~<br><!-- End of picture text -->



<!-- Start of picture text -->
PSEHs os: SEEM<br><!-- End of picture text -->

# Long QT Syndrome 

**Clinical Focus:** A disorder of the heart's electrical recharging system. The key metric is the Corrected QT interval (QTc). **The Detection Rule:** The QT interval must be corrected for heart rate dependency (QT contracts as HR increases). **Thresholds:** 

- Men: QTc > 440 ms. 

- • Women: QTc > 460 ms. 



<!-- Start of picture text -->
H|<br>9> s<br>QT Interval<br>QTc =  O T<br>VRR<br><!-- End of picture text -->



<!-- Start of picture text -->
es<br>05:<br><!-- End of picture text -->

Technical Approach: Semantic Segmentation as a Foundation **Our Method:** Treating 1D ECG as a segmentation task for pointwise classification. **Target Classes:** The model classifies every point into P-wave, QRS, T-wave, or Background. ECG Signal Analysis a ee ee ee **The Benefit:** Enables precise, automated ee ee RRR Eee extraction of clinical metrics RR | eee (intervals & amplitudes). ee eee LET TT PEt tT iT tT tt **P** RN TT TT 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Theory 

##### **ECG Signal Acquisition:** 

   - A Holter monitor records 12-lead ECG signals for 24 hours 

- Each lead captures the electrical activity of the heart from a different angle 

- **Signal Processing:** 

   - Raw ECG data is filtered to remove noise and baseline drift 

   - The signal is normalized and segmented for further analysis 

- **AI-Based Classification:** 

   - Processed ECG segments are fed into a trained neural network 

   - The model analyzes patterns and identifies clinically meaningful events 



<!-- Start of picture text -->
EEHS OSL<br><!-- End of picture text -->

# IDEs & Components 

- **Python Environment:** used for implementing the ECG processing pipeline and training the machine-learning model 

- • **VS Code & Git:** used for development, version control, and collaborative f 5 : 0 ' 

- coding ' 

- **Local PC GPU:** used for accelerating deep-learning training and handling large ECG dataset 



<!-- Start of picture text -->
Be5 ose Bee<br><!-- End of picture text -->

# Block Diagram 

**AI Diagnosis Logic: Holter** aggregates **Classification: Monitor: Preprocessing:** classification analyzes ECG records 24-hour filters, normalizes, results to segments using a 12-lead ECG and segments the determine the trained neural ECG signals network clinical diagnosis 



# Data Foundation: Two Key Databases 

**1. LUDB Database:** 

- Diverse ECG morphologies. 

- • Per-Lead annotation. 

- 200 ECG records 

- Each record 10 seconds 



<!-- Start of picture text -->
LUDB: PER-LEAD ANNOTATION<br>oi =§=—h<br>tytA1 te+A2 ts-A3 tytA4 ts+AS te AG<br>| = =|<br>5i<br><!-- End of picture text -->

**2. ISP Database:** 

- Real-world clinical data. 

- • Global annotation. 

- 475 ECG records. 

- Each record 10 seconds 



<!-- Start of picture text -->
ISP: GLOBAL ANNOTATION<br>o_o. €@ &<br>— a= fs ae<br>te start trend tors_stat tarsend trstart trend<br>te_stat teend tars stat tars_end tr_start trend<br>= |<br>nom @ &<br>testat trend tors_stat torsend tr_start trens<br><!-- End of picture text -->



# Data Preprocessing Pipeline 

**1. Resampling:** Downsampling signals from 500 Hz to 128 Hz. **2. Filtering:** Applied Bandpass (0.5–63 Hz) and Notch (50 Hz) filters. **3. Normalization:** Z-score standardization applied independently per lead. **4. Segmentation:** Fixed-length windows of 1280 samples (10 seconds). 



<!-- Start of picture text -->
A bl | I RAWECG INPUT<br>[Aah Aan Avr Aas (e.g., 500Hz)<br>RESAMPLING<br>(to 128Hz)<br>(Bandpass/Notch)<br>[RF FILTERING<br>a | NORMALIZATION(Z-score per lead)<br>WINDOWING<br>(1280 samples/ 10s)<br><!-- End of picture text -->



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Implemented Deep Learning Models: Overview 

**1. U-Net:** Industry standard for biomedical image segmentation. **2. SCFNet:** Designed for enhanced multi-scale feature integration. **3. Ensemble Model:** Weighted combination of U-Net and SCFNet predictions to leverage the strengths of both. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Model 1 Architecture: 1D U-Net 

###### **Standard Encoder-Decoder Structure:** 

- Adapted from medical imaging to 1D signal processing, extracting deep morphological features while maintaining temporal resolution. 

- **Attention Gates (AGs):** 

- Integrated into Skip Connections to actively filter irrelevant noise and suppress background activity. 



<!-- Start of picture text -->
EE 5 05.Eee<br><!-- End of picture text -->



<!-- Start of picture text -->
Bottleneck<br>Features<br>e<br>Input ECG a al ae Probability Mask<br>(12, 1280) Encoder 1 ~<a Attention y Decoder 1 (4, 1280) |<br><!-- End of picture text -->

Model 1 Architecture: 1D U-Net 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Model 2 Architecture: 1D SCFNet 

**Dual-Stream Design:** 

• Simultaneously extracts local high-frequency features (sharp QRS peaks) and global contextual patterns (rhythmic P and T waves). **SCF (Skip-Cat-Fusion) Blocks:** 

- Replaces standard skip connections with an adaptive mechanism that learns the optimal fusion of multi-scale features. 



<!-- Start of picture text -->
BSE<br>1s os: EERE<br><!-- End of picture text -->



<!-- Start of picture text -->
Local Stream<br>(Conv1D)<br>Input ECG Fusion Probability Mask<br>(12, 1280) Split Module (4, 1280)<br>Global Stream<br>(Bi-LSTM)<br><!-- End of picture text -->

Model 2 Architecture: 1D SCFNet 



<!-- Start of picture text -->
Ee1s 05. Eee<br><!-- End of picture text -->

# Model 3 Architecture: Ensemble Strategy 

• **Objective:** Reduce prediction variance and enhance overall generalization across unseen data. • **Methodology:** Direct weighted averaging of the Softmax Probability Maps. 

• **Synergy:** Combines the precise boundary localization of U-Net with the morphological robustness of SCFNet. 

The final prediction is a weighted sum of U-Net and SCFNet outputs: 



<!-- Start of picture text -->
Priel — «x Firvncs tr (1 — a) ° Pscrnet<br><!-- End of picture text -->



<!-- Start of picture text -->
BeeneHs 05h<br><!-- End of picture text -->



<!-- Start of picture text -->
U-Net<br>Output _<br>(Probability<br>Map) Weighted Average:<br>a* Punet Final<br>‘ EY Ensemble<br>SCENet (1-a) * scent Segmentation<br>(ProbabilityOutput  =<br>Map)<br><!-- End of picture text -->

Model 3 Architecture: Ensemble Strategy 



<!-- Start of picture text -->
Bee1s os. SEEN<br><!-- End of picture text -->

## Training Strategy: Loss Function & Class Imbalance 

**Challenge:** Extreme imbalance between dominant background and short wave segments (P, QRS, T). **Solution:** 50/50 Composite Loss function (Dice + Weighted Cross Entropy). 

- **Dice Loss:** Maximizes spatial overlap for precise wave boundaries. 

- **Weighted CE:** Prioritizes minority wave classes using higher weights (up to 2.0). 



<!-- Start of picture text -->
Challenge: Severe<br>|____ECG Class Distribution (Per Heartbeat) Class Imbalance<br>Background T-wave eee er<br>(>70%) (~20%)<br>QRS<br>P-wave Complex<br>(~5%) — (<5%)<br><!-- End of picture text -->



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Data Augmentation Strategy 

**Goal:** Enhance model robustness and prevent overfitting by artificially increasing training data diversity during training. **Techniques Applied:** 

**1. Noise Injection:** Gaussian Noise and Baseline Wander (simulating respiratory artifacts). 

**2. Hardware Failures:** Amplitude Scaling and Channel Dropout (electrode faults). **3. Holter Emulation:** Low-Frequency Simulation to bridge hardware domain gaps. 



# Training Optimization 

**Optimization Engine:** AdamW optimizer featuring decoupled Weight Decay for robust regularization. **Learning Rate:** CosineAnnealingLR scheduler for continuous and smooth fine-tuning. **Full Convergence:** Purposely disabled Early Stopping. Models were trained for full 50100 epochs to ensure complete optimization. 



<!-- Start of picture text -->
ass Fnctonsror<br>EARLY(Best STOPPINGGeneralization)POINT<br><!-- End of picture text -->



<!-- Start of picture text -->
Bey5 051<br><!-- End of picture text -->

Feature Engineering: Temporal Derivatives **Input Expansion:** Increased model input from 12 to 24 channels. **Added Features:** The 12 new channels represent the first derivative (dV/dt) of each raw lead. **Purpose:** explicitly captures signal slope and rate of change. **Benefit:** Improves detection of rapid morphological transitions DERIVATIVE FEATURE: Explicitly Capturing Steep (e.g., sharp QRS peaks). 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

Performance Evaluation Metrics **Segmentation Quality:** Evaluated using Dice Score (F1-equivalent) to measure spatial overlap. **Timing Accuracy:** Measured by Mean Absolute Error (MAE) in milliseconds. **Robustness:** Analysis of standard deviation and error distributions. **Generalization:** Cross-dataset testing between LUDB and ISP databases. 





<!-- Start of picture text -->
Same-Dataset Performance (Trained on X, Tested on X)<br>1.0 Mmm P-wave<br>0.9089 Mmm QRS<br>x mm T-wave<br>C= Mean<br>0.8<br>2 0.6<br>fo}<br>a<br>2aov<br>0.4<br>0.2<br>0.0<br>NE7 (Wo!8) + W)pB) (wiD8) er (\sP) er (\sP. Le \oP)<br>gcrNnE ensemert UN scr’ ensen®<br><!-- End of picture text -->

Segmentation Performance (Dice Score) 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Analyzing Segmentation Results 

**QRS Complex:** Highest accuracy due to sharp morphology and high amplitude. **P-wave:** Most challenging class. **T-wave:** Reliable detection, but boundary ambiguity affects precise timing. 



<!-- Start of picture text -->
GS/sLA 05. aesEES<br><!-- End of picture text -->



<!-- Start of picture text -->
Cross-Dataset: ISP > LUDB (Trained on ISP, Tested on LUDB)<br>1.0 lm P-wave<br>mmm QRS<br>mm T-wave<br>0.7835 Ea Mean<br>08 A<br>2 06<br>8<br>raa<br>a<br>0.4<br>0.2<br>0.0<br>net (sr) cee+ us?) evsenou0s)<br><!-- End of picture text -->



<!-- Start of picture text -->
Cross-Dataset: LUDB — ISP (Trained on LUDB, Tested on ISP)<br>1.0 lm P-wave<br>Mm QRS<br>mmm T-wave<br>mm Mean<br>0.8 0.7542<br>2 06<br>8<br>ra<br>a<br>a<br>0.4<br>0.2<br>0.0<br>ynet 08) covet wi8) evs are O yo8)<br><!-- End of picture text -->

Domain Shift Challenge 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Overcoming Domain Shift 

**The Challenge:** Single-dataset models suffered a 15% performance drop on unseen data. **The Solution:** Combined Training (LUDB + ISP) and Data Augmentation. **Result:** Stable performance exceeding 90% Dice score across all clinical datasets. **Feature Engineering:** Temporal derivatives (dV/dt) proved critical for model stability. 



<!-- Start of picture text -->
Be] v'sev 05. AaSESE SE<br><!-- End of picture text -->



<!-- Start of picture text -->
Cross-Dataset Generalization Comparison<br>U-Net (Mean Dice %) SCFNet (Mean Dice %) Ensemble (Mean Dice %)<br>95.0 95.0 95.0<br>LUDB 75.0% 92.5 LupB 73.6% 92.5 UDB 75.4% 92.5<br>90.0 90.0 90.0<br>IsP 78.4% 87.5 ISP 76.0% 87.5 ISP 76.4% 87.5<br>% 23 23 ES<br>Ffs 2sFf 2sa g<br>= 85.09 85.09 o 85.09<br>Z ce ae 6<br>7s c=5 cess= ©5<br>e£ =oe =ae =&<br>COMBINED 82.5 COMBINED 82.5 COMBINED 82.5<br>80.0 80.0 80.0<br>COMBINED_DERIV 7715 COMBINED_DERIV 88.2% 715 COMBINED_DERIV 715<br>LuDB 75.0 75.0 75.0<br>Test Dataset IsP UDB Test Dataset IsP LUDB Test Dataset IsP<br><!-- End of picture text -->

Overcoming Domain Shift 



<!-- Start of picture text -->
Bret<br>Vee1's 0S. CesT)a<br><!-- End of picture text -->



<!-- Start of picture text -->
QTc MAE — Bazett Formula (QTc = QT / VRR_sec, units: ms)<br>U-Net — QTc MAE (Bazett) so SCFNet — QTc MAE (Bazett) so Ensemble — QTc MAE (Bazett) So<br>LWDB 48.7 WDB 35.9 LUDB 41.8<br>40 40 40<br>7 IsP - IsP 36.6 oy ISP. 35.0<br>8 30_ 8 30_ 3 30<br>: Eg Eg E<br>é 2 8 2 8 ra<br>2 = 2 =P =<br>= zx = zx: z<br>£ 2? E 2° 8 20°<br>F COMBINED F COMBINED F COMBINED<br>10 10 10<br>COMBINED_DERIV COMBINED_DERIV COMBINED_DERIV<br>LUDB ISP. oO LUDB ISP. 0 LUDB ISP 0<br>Test Dataset Test Dataset Test Dataset<br><!-- End of picture text -->

Overcoming Domain Shift 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Analyzing Interval Timing Errors 

**Error Distribution:** Evaluated across key clinical intervals including QT and QTc. **Gaussian Profile:** Most timing errors center closely around zero, demonstrating high algorithmic precision. **T-offset Challenge:** Higher variance observed due to the gradual morphological of the T-wave boundary. 



<!-- Start of picture text -->
Bee<br>1s os. SEEN<br><!-- End of picture text -->



<!-- Start of picture text -->
Ensemble | COMBINED_DERIV ~ ISP<br>MAE=15.7 ms (all beats), n=848<br>0.08 7 shapiro p<0.001 ' ___. Gaussian<br>' H=+7.0, 0=18.2<br>0.07 f --- Mean<br>1<br>0.06 '<br>!<br>1<br>0.05 '<br>><br>2 0.04 {<br>&<br>0.03<br>1<br>\<br>0.02 A i fi<br>oop + | aS<br>son i il<br>—60 —40 —20 ie) 20 40 60<br>QT Error (ms)<br><!-- End of picture text -->



<!-- Start of picture text -->
Ensemble | COMBINED_DERIV > LUDB<br>MAE=21.8 ms (all beats), n=175<br>0.05 1 Shapiro p<0.001 i Gaussian<br>— [1=-3.0, 0=29.1<br>--- Mean<br>0.04<br>> 0.03<br>2<br>g<br>0.02<br>0.01<br>0.00 Let | ~~<br>al ih<br>-75 —50 —25 0 25 50 75 100<br>QT Error (ms)<br><!-- End of picture text -->

Analyzing Interval Timing Errors 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Hardware Limits 

**Quantization Error:** 128 Hz sampling rate limits precision to 7.8 ms increments. **High-Frequency Track:** 500 Hz training reduced MAE to 14.04 ms. **Conclusion:** The current "accuracy ceiling" is a hardware limitation, not an algorithmic flaw. **Clinical Impact:** Precise T-offset remains the most sensitive metric to hardware resolution. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Inference & Continuous Analysis 

**Scalability:** Processing 24-hour recordings (~11 million samples per lead). **Sliding Window:** 10-second analysis segments with **50% overlap** . **Stability Filtering:** Automated rejection of noisy segments and baseline drift. **Performance:** Fully accelerated GPU pipeline for fast clinical turnaround. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Clinical Logic & Post-Processing 

**HR Stability Filter:** Rejects segments where heart rate fluctuates > 10 BPM. **Local Averaging:** QTc is calculated as a mean of 10 stable neighbors. **Risk Categorization:** Patients classified into Normal, Borderline, or Prolonged LQT. **Disease Burden:** Summary report quantifies the percentage of high-risk heartbeats. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Real-World Clinical Validation 

**Pilot Test:** Validated on 24-hour recordings from Rambam hospital. **Systematic Bias:** Observed a consistent ~30ms offset between AI and manual readings. **Cause Analysis:** Gap between training data (public databases) and realworld recordings, including differences in wave morphology, noise profiles, and hardware-specific signal processing. **Next Steps:** Acquisition of more clinical data to verify if the bias is constant and justify a systematic calibration shift. 



<!-- Start of picture text -->
BeesHS 05k<br><!-- End of picture text -->



<!-- Start of picture text -->
Holter ECG ¢ Wave Visualization * 48.2h<br>me we ei Be ee ee ee<br>= 2 Lo<br>20.3 NS eo ah Oe  _U"'"”<br><!-- End of picture text -->

ECGViewer: Clinical Interface and Visualization 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Key Challenges 

**Hardware Constraints:** 128 Hz sampling rate limits temporal resolution to 7.8ms increments (Quantization Error). **Morphological Ambiguity:** Detecting the "elusive" T-offset due to its gradual return to the isoelectric line. **Domain Shift:** Significant performance variance between public academic datasets and real-world clinical hardware. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

### Clinical Database for Brugada Syndrome Classification 

- **Data source:** Commercial Holter recordings in ISHNE format, with paired XML annotation files (.arrexp.xml) labeled by cardiologists at Rambam Health Care Campus. 

- **Window extraction:** Clinical XML annotations were parsed to isolate Brugada Type 1 events only, filtering out borderline cases. ~10-second windows were extracted on the leads where the syndrome appears: V1, V2, V3 (and V5, V6 for Brugada HL annotations). 

- **Sample size:** Extraction was performed on Brugada patients, yielding 273 windows in total. 

42 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Conclusions 

**End-to-End Pipeline:** Automated 24h Holter analysis from raw ISHNE files to clinical risk reports. **Domain Shift Resolved:** Combined training achieved stable >90% Dice scores, overcoming the 15% cross-dataset drop. **Hardware-Bound Accuracy:** Timing errors are limited by 128 Hz quantization (7.8 ms floor), not the algorithm. 

**Clinical Bias:** Detected a consistent ~30 ms offset; deferred permanent correction pending larger datasets. **Brugada Foundation:** Established data extraction infrastructure for future classification models. 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Our Project Scope 

We are implementing the machine learning research phase including: 

- Understanding the physical and medical problem 

- • Exploring the data space and relevant signal heuristics • Researching ML methods for Holter ECG analysis • Creating a unified data lake for future development • Performing feature selection and methodology comparison 



<!-- Start of picture text -->
EeeW'S OSL<br><!-- End of picture text -->

# Future Work 

###### **Long QT Syndrome Track:** 

- Investigate original hardware files to bypass the Quantization Error ceiling. 

- Acquire more clinical data to validate the ~30ms bias and calibrate filters. 

- • Apply clinical Fine-Tuning to bridge the academic-to-real-world data gap. 

- **Brugada Syndrome Track:** 

- Extract healthy control datasets using an identical preprocessing pipeline. 

- • Construct a binary classifier leveraging the existing segmentation architecture as a Backbone. 

