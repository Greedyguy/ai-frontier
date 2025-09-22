# TESSERA: Precomputed FAIR Global Pixel Embeddings for Earth Representation and Analysis

**Korean Title:** TESSERA: 지구 표현 및 분석을 위한 사전 계산된 FAIR 글로벌 픽셀 임베딩

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Pixel-oriented Foundation Model|Pixel-oriented Foundation Model]] [[keywords/specific/Few-shot Learning|Few-shot Learning]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/broad/Earth Observation|Earth Observation]] [[keywords/unique/TESSERA|TESSERA]] [[categories/cs.LG|cs.LG]] [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet: A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (79.0% similar) [[2025-09-22/Sea-ing Through Scattered Rays_ Revisiting the Image Formation Model for Realistic Underwater Image Generation_20250922|Sea-ing Through Scattered Rays: Revisiting the Image Formation Model for Realistic Underwater Image Generation]] (78.8% similar) [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pixel-oriented Foundation Model
**🔗 Specific Connectable**: Few-shot Learning
**🔬 Broad Technical**: Machine Learning, Earth Observation
**⭐ Unique Technical**: TESSERA
## 🔗 유사한 논문
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (79.0% similar)
- [[2025-09-22/Sea-ing Through Scattered Rays_ Revisiting the Image Formation Model for Realistic Underwater Image Generation_20250922|Sea-ing Through Scattered Rays Revisiting the Image Formation Model for Realistic Underwater Image Generation]] (78.8% similar)
- [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek Training-Free Spatial Prompting for Multimodal Large Language Model]] (78.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (78.1% similar)
- [[2025-09-22/Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification_20250922|Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification]] (77.8% similar)


**ArXiv ID**: [2506.20380](https://arxiv.org/abs/2506.20380)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.20380.pdf)


**ArXiv ID**: [2506.20380](https://arxiv.org/abs/2506.20380)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.20380.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pixel-oriented Foundation Model
**🔗 Specific Connectable**: Few-shot Learning
**⭐ Unique Technical**: TESSERA
**🔬 Broad Technical**: Machine Learning, Earth Observation

## 🏷️ 추출된 키워드



`Machine Learning` • 

`Earth Observation` • 

`Few-shot Learning` • 

`Multilayer Perceptron` • 

`TESSERA`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20380v5 Announce Type: replace 
Abstract: Petabytes of satellite Earth Observation (EO) data are freely available and can address critical global challenges. However, EO data quality is poor due to clouds and variable lighting conditions. To address this, practitioners typically use compositing, but this critically removes the temporal phenological signal. Moreover, supervised machine learning to map composited pixels to task-specific classes requires accurately labelled data that are rarely available. We present TESSERA, a pixel-oriented foundation model for EO time series that creates 128-dimensional latent embeddings requiring only a few labels for task-specific training to achieve state-of-the-art performance across diverse complex tasks. TESSERA uses two encoders that combine optical data with synthetic aperture radar backscatter coefficients at 10m resolution, creating embeddings fused with a multilayer perceptron to generate annual global embedding maps. TESSERA closely matches or outperforms state-of-the-art task-specific models and other foundation models across five diverse downstream tasks. It is unprecedented in ease of use, scale, and accuracy: no other open foundation model provides precomputed outputs with global, annual coverage at 10m resolution.

## 🔍 Abstract (한글 번역)

arXiv:2506.20380v5 발표 유형: 교체  
초록: 페타바이트의 위성 지구 관측(EO) 데이터가 무료로 제공되며, 이는 중요한 글로벌 문제를 해결할 수 있습니다. 그러나 EO 데이터의 품질은 구름과 가변적인 조명 조건 때문에 좋지 않습니다. 이를 해결하기 위해 실무자들은 일반적으로 합성을 사용하지만, 이는 중요한 시간적 생태 신호를 제거합니다. 게다가, 합성된 픽셀을 작업별 클래스에 매핑하기 위한 지도 학습은 정확하게 라벨링된 데이터가 거의 없기 때문에 어렵습니다. 우리는 EO 시계열을 위한 픽셀 지향 기초 모델인 TESSERA를 제시합니다. 이 모델은 작업별 학습을 위해 몇 개의 라벨만 필요로 하며, 다양한 복잡한 작업에서 최첨단 성능을 달성하기 위해 128차원 잠재 임베딩을 생성합니다. TESSERA는 10m 해상도의 합성 개구 레이더 후방 산란 계수와 광학 데이터를 결합하는 두 개의 인코더를 사용하여, 다층 퍼셉트론과 융합된 임베딩을 생성하여 연간 글로벌 임베딩 지도를 만듭니다. TESSERA는 다섯 가지 다양한 다운스트림 작업에서 최첨단 작업별 모델 및 기타 기초 모델과 비슷하거나 더 나은 성능을 보입니다. 사용의 용이성, 규모 및 정확성 면에서 전례가 없으며, 다른 공개 기초 모델은 10m 해상도로 전 세계 연간 커버리지를 제공하는 사전 계산된 출력을 제공하지 않습니다.

## 📝 요약

위성 지구 관측(EO) 데이터는 글로벌 문제 해결에 유용하지만, 구름과 조명 변화로 인해 품질이 낮습니다. 이를 해결하기 위해 합성 기법이 사용되지만, 이는 시간적 신호를 제거합니다. 또한, 합성된 데이터를 지도 학습에 활용하려면 정확한 라벨이 필요한데, 이는 드뭅니다. TESSERA는 EO 시계열을 위한 픽셀 기반 모델로, 소수의 라벨만으로도 다양한 복잡한 작업에서 최첨단 성능을 발휘합니다. 이 모델은 광학 데이터와 합성 개구 레이더 데이터를 결합하여 128차원의 잠재 임베딩을 생성하고, 연간 글로벌 임베딩 지도를 만듭니다. TESSERA는 다섯 가지 다양한 작업에서 기존 모델을 능가하거나 대등한 성능을 보이며, 사용의 용이성, 규모, 정확성 면에서 독보적입니다. 10m 해상도로 전 세계 연간 커버리지의 사전 계산된 출력을 제공하는 공개 모델은 없습니다.

## 🎯 주요 포인트


- 1. 위성 지구 관측 데이터의 품질 문제를 해결하기 위해 TESSERA라는 픽셀 기반 기초 모델을 제안합니다.

- 2. TESSERA는 128차원 잠재 임베딩을 생성하며, 소량의 레이블만으로도 다양한 복잡한 작업에서 최첨단 성능을 달성합니다.

- 3. 이 모델은 광학 데이터와 합성 개구 레이더 후방 산란 계수를 결합하여 연간 글로벌 임베딩 지도를 생성합니다.

- 4. TESSERA는 다섯 가지 다양한 다운스트림 작업에서 기존의 최첨단 모델과 다른 기초 모델을 능가하거나 그에 필적하는 성능을 보입니다.

- 5. TESSERA는 사용의 용이성, 규모, 정확성 면에서 전례가 없으며, 10m 해상도로 전 세계 연간 범위를 제공하는 유일한 개방형 기초 모델입니다.


---

*Generated on 2025-09-22 15:59:48*