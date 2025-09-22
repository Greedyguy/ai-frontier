# BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings

**Korean Title:** BabyHuBERT: 아동 중심의 장기 녹음에서 화자를 분할하기 위한 다국어 자기 지도 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Théo Charlot|Théo Charlot]] [[authors/Tarek Kunze|Tarek Kunze]] [[authors/Maxime Poli|Maxime Poli]] [[authors/Alejandrina Cristia|Alejandrina Cristia]] [[authors/Emmanuel Dupoux|Emmanuel Dupoux]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multilingual Child Speech Analysis

## 🔗 유사한 논문
- [[UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (76.6% similar)
- [[TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (76.5% similar)
- [[Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (75.9% similar)
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (75.5% similar)
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (75.0% similar)

## 📋 저자 정보

**Authors:** Théo Charlot, Tarek Kunze, Maxime Poli, Alejandrina Cristia, Emmanuel Dupoux, Marvin Lavechin

## 📄 Abstract (원문)

Child-centered long-form recordings are essential for studying early language
development, but existing speech models trained on clean adult data perform
poorly due to acoustic and linguistic differences. We introduce BabyHuBERT, the
first self-supervised speech representation model trained on 13,000 hours of
multilingual child-centered long-form recordings spanning over 40 languages. We
evaluate BabyHuBERT on speaker segmentation, identifying when target children
speak versus female adults, male adults, or other children -- a fundamental
preprocessing step for analyzing naturalistic language experiences. BabyHuBERT
achieves F1-scores from 52.1% to 74.4% across six diverse datasets,
consistently outperforming W2V2-LL4300 (trained on English long-forms) and
standard HuBERT (trained on clean adult speech). Notable improvements include
13.2 absolute F1 points over HuBERT on Vanuatu and 15.9 points on Solomon
Islands corpora, demonstrating effectiveness on underrepresented languages. By
sharing code and models, BabyHuBERT serves as a foundation model for child
speech research, enabling fine-tuning on diverse downstream tasks.

## 🔍 Abstract (한글 번역)

아동 중심의 장시간 녹음은 초기 언어 발달을 연구하는 데 필수적이지만, 기존의 성인 데이터를 기반으로 훈련된 음성 모델은 음향 및 언어적 차이로 인해 성능이 저조합니다. 우리는 40개 이상의 언어에 걸쳐 13,000시간의 다국어 아동 중심 장시간 녹음으로 훈련된 최초의 자가 지도 음성 표현 모델인 BabyHuBERT를 소개합니다. 우리는 BabyHuBERT를 화자 분할, 즉 목표 아동이 여성 성인, 남성 성인 또는 다른 아동과 비교하여 언제 말하는지를 식별하는 데 평가합니다. 이는 자연스러운 언어 경험을 분석하기 위한 기본적인 전처리 단계입니다. BabyHuBERT는 6개의 다양한 데이터셋에서 52.1%에서 74.4%의 F1 점수를 기록하며, 일관되게 W2V2-LL4300(영어 장시간 녹음으로 훈련됨) 및 표준 HuBERT(깨끗한 성인 음성으로 훈련됨)를 능가합니다. 주목할 만한 개선 사항으로는 Vanuatu 코퍼스에서 HuBERT보다 13.2의 절대 F1 포인트, Solomon Islands 코퍼스에서 15.9 포인트의 향상을 보여주며, 이는 대표성이 부족한 언어에서의 효과성을 입증합니다. 코드와 모델을 공유함으로써, BabyHuBERT는 아동 음성 연구의 기초 모델로서 다양한 후속 작업에 대한 미세 조정을 가능하게 합니다.

## 📝 요약

BabyHuBERT는 40개 이상의 언어로 구성된 13,000시간의 아동 중심 장기 녹음을 기반으로 훈련된 최초의 자가 지도 학습 음성 표현 모델입니다. 이 모델은 아동의 자연스러운 언어 경험을 분석하기 위한 기초 단계인 화자 분할 작업에서 뛰어난 성능을 보입니다. BabyHuBERT는 6개의 다양한 데이터셋에서 F1 점수 52.1%에서 74.4%를 기록하며, 기존의 W2V2-LL4300 및 HuBERT 모델보다 일관되게 우수한 성능을 발휘합니다. 특히, Vanuatu와 Solomon Islands 코퍼스에서 각각 13.2점과 15.9점의 F1 점수 향상을 보여, 저대표 언어에서도 효과적임을 입증했습니다. BabyHuBERT는 아동 음성 연구의 기초 모델로서 다양한 후속 작업에 활용될 수 있도록 코드와 모델을 공유합니다.

## 🎯 주요 포인트

- 1. BabyHuBERT는 40개 이상의 언어를 포함한 13,000시간의 아동 중심 장기 녹음을 기반으로 훈련된 최초의 자가 지도 학습 음성 표현 모델입니다.

- 2. BabyHuBERT는 아동, 여성 성인, 남성 성인, 다른 아동을 구분하는 화자 분할 작업에서 기존 모델보다 우수한 성능을 보입니다.

- 3. BabyHuBERT는 다양한 데이터셋에서 F1 점수 52.1%에서 74.4%까지 달성하며, 특히 저대표 언어인 바누아투와 솔로몬 제도 코퍼스에서 큰 개선을 보였습니다.

- 4. BabyHuBERT는 아동 음성 연구의 기초 모델로서 다양한 후속 작업에 대한 미세 조정을 가능하게 합니다.

- 5. 코드와 모델을 공유함으로써 BabyHuBERT는 자연스러운 언어 경험 분석의 필수적인 전처리 단계에서 유용하게 사용될 수 있습니다.

---

*Generated on 2025-09-20 01:38:05*