# Hala Technical Report: Building Arabic-Centric Instruction & Translation Models at Scale

**Korean Title:** 할라 기술 보고서: 대규모 아랍어 중심의 교육 및 번역 모델 구축

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Hasan Abed Al Kader Hammoud|Hasan Abed Al Kader Hammoud]] [[authors/Mohammad Zbeeb|Mohammad Zbeeb]] [[authors/Bernard Ghanem|Bernard Ghanem]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Translate and Tune Pipeline

## 🔗 유사한 논문
- [[Apertus_ Democratizing Open and Compliant LLMs for Global Language Environments_20250917|Apertus Democratizing Open and Compliant LLMs for Global Language Environments]] (79.9% similar)
- [[MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (79.4% similar)
- [[Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (79.2% similar)
- [[CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (78.9% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (78.8% similar)

## 📋 저자 정보

**Authors:** Hasan Abed Al Kader Hammoud, Mohammad Zbeeb, Bernard Ghanem

## 📄 Abstract (원문)

We present Hala, a family of Arabic-centric instruction and translation
models built with our translate-and-tune pipeline. We first compress a strong
AR$\leftrightarrow$EN teacher to FP8 (yielding $\sim$2$\times$ higher
throughput with no quality loss) and use it to create high-fidelity bilingual
supervision. A lightweight language model LFM2-1.2B is then fine-tuned on this
data and used to translate high-quality English instruction sets into Arabic,
producing a million-scale corpus tailored to instruction following. We train
Hala models at 350M, 700M, 1.2B, and 9B parameters, and apply slerp merging to
balance Arabic specialization with base-model strengths. On Arabic-centric
benchmarks, Hala achieves state-of-the-art results within both the "nano"
($\leq$2B) and "small" (7-9B) categories, outperforming their bases. We release
models, data, evaluation, and recipes to accelerate research in Arabic NLP.

## 🔍 Abstract (한글 번역)

Hala는 번역 및 튜닝 파이프라인을 통해 구축된 아랍어 중심의 지시 및 번역 모델군을 소개합니다. 우리는 먼저 강력한 AR$\leftrightarrow$EN 교사를 FP8로 압축하여 품질 손실 없이 약 2배의 처리량을 달성하고, 이를 사용하여 고품질의 이중 언어 감독을 생성합니다. 그런 다음 경량 언어 모델 LFM2-1.2B를 이 데이터로 미세 조정하여 고품질의 영어 지시 세트를 아랍어로 번역하여 지시 따르기에 맞춘 백만 규모의 코퍼스를 생성합니다. 우리는 Hala 모델을 350M, 700M, 1.2B 및 9B 매개변수로 훈련하고, slerp 병합을 적용하여 아랍어 특화와 기본 모델의 강점을 균형 있게 조정합니다. 아랍어 중심의 벤치마크에서 Hala는 "nano" (≤2B) 및 "small" (7-9B) 카테고리 모두에서 최첨단 결과를 달성하며, 기본 모델을 능가합니다. 우리는 아랍어 NLP 연구를 가속화하기 위해 모델, 데이터, 평가 및 레시피를 공개합니다.

## 📝 요약

Hala는 아랍어 중심의 지시 및 번역 모델로, translate-and-tune 파이프라인을 통해 개발되었습니다. 강력한 AR↔EN 교사를 FP8로 압축하여 처리량을 두 배로 늘리면서 품질 손실 없이 고품질의 이중 언어 데이터를 생성했습니다. 이 데이터를 바탕으로 경량 언어 모델 LFM2-1.2B를 미세 조정하여 영어 지시문을 아랍어로 번역, 지시문에 특화된 백만 규모의 코퍼스를 제작했습니다. Hala 모델은 350M, 700M, 1.2B, 9B 매개변수로 훈련되었으며, slerp 병합을 통해 아랍어 특화와 기본 모델의 강점을 균형 있게 조정했습니다. 아랍어 중심 벤치마크에서 Hala는 "nano" (≤2B) 및 "small" (7-9B) 카테고리에서 최첨단 성능을 달성했습니다. 모델, 데이터, 평가 및 레시피를 공개하여 아랍어 NLP 연구를 가속화하고자 합니다.

## 🎯 주요 포인트

- 1. Hala는 번역 및 튜닝 파이프라인을 통해 개발된 아랍어 중심의 명령 및 번역 모델입니다.

- 2. FP8로 압축된 AR↔EN 교사를 사용하여 고품질의 이중 언어 감독 데이터를 생성합니다.

- 3. LFM2-1.2B 언어 모델을 미세 조정하여 영어 명령 세트를 아랍어로 번역하고, 명령 수행에 맞춘 백만 규모의 코퍼스를 만듭니다.

- 4. Hala 모델은 350M, 700M, 1.2B, 9B 파라미터로 훈련되며, slerp 병합을 통해 아랍어 전문성과 기본 모델의 강점을 균형 있게 조정합니다.

- 5. Hala는 아랍어 중심 벤치마크에서 최첨단 성능을 달성하며, "nano" (≤2B) 및 "small" (7-9B) 카테고리에서 기반 모델을 능가합니다.

---

*Generated on 2025-09-20 09:19:18*