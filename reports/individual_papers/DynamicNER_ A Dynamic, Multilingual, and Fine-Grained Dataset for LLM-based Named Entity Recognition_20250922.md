# DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition

**Korean Title:** 다이나믹NER: 대규모 언어 모델 기반 명명된 개체 인식을 위한 동적, 다국어 및 세분화된 데이터셋

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multilingual NER

## 🔗 유사한 논문
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.0% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.6% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (82.8% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.11022v5 Announce Type: replace-cross 
Abstract: The advancements of Large Language Models (LLMs) have spurred a growing interest in their application to Named Entity Recognition (NER) methods. However, existing datasets are primarily designed for traditional machine learning methods and are inadequate for LLM-based methods, in terms of corpus selection and overall dataset design logic. Moreover, the prevalent fixed and relatively coarse-grained entity categorization in existing datasets fails to adequately assess the superior generalization and contextual understanding capabilities of LLM-based methods, thereby hindering a comprehensive demonstration of their broad application prospects. To address these limitations, we propose DynamicNER, the first NER dataset designed for LLM-based methods with dynamic categorization, introducing various entity types and entity type lists for the same entity in different context, leveraging the generalization of LLM-based NER better. The dataset is also multilingual and multi-granular, covering 8 languages and 155 entity types, with corpora spanning a diverse range of domains. Furthermore, we introduce CascadeNER, a novel NER method based on a two-stage strategy and lightweight LLMs, achieving higher accuracy on fine-grained tasks while requiring fewer computational resources. Experiments show that DynamicNER serves as a robust and effective benchmark for LLM-based NER methods. Furthermore, we also conduct analysis for traditional methods and LLM-based methods on our dataset. Our code and dataset are openly available at https://github.com/Astarojth/DynamicNER.

## 🔍 Abstract (한글 번역)

arXiv:2409.11022v5 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)의 발전은 명명된 개체 인식(NER) 방법에 대한 관심을 증가시켰습니다. 그러나 기존 데이터셋은 주로 전통적인 기계 학습 방법에 맞춰 설계되어 있으며, 말뭉치 선택과 전체 데이터셋 설계 논리 측면에서 LLM 기반 방법에는 부적합합니다. 또한, 기존 데이터셋의 고정적이고 상대적으로 조잡한 개체 분류는 LLM 기반 방법의 뛰어난 일반화 및 맥락 이해 능력을 적절히 평가하지 못하여 이들의 광범위한 응용 가능성을 포괄적으로 보여주는 데 장애가 됩니다. 이러한 한계를 해결하기 위해, 우리는 LLM 기반 방법을 위해 설계된 첫 번째 NER 데이터셋인 DynamicNER를 제안합니다. 이 데이터셋은 동적 분류를 통해 다양한 개체 유형과 서로 다른 맥락에서 동일한 개체에 대한 개체 유형 목록을 도입하여 LLM 기반 NER의 일반화를 보다 잘 활용합니다. 이 데이터셋은 또한 다국어 및 다중 세분화로, 8개 언어와 155개 개체 유형을 포함하며, 다양한 분야의 말뭉치를 포괄합니다. 더 나아가, 우리는 두 단계 전략과 경량 LLM에 기반한 새로운 NER 방법인 CascadeNER를 소개하여, 더 적은 계산 자원을 필요로 하면서도 세분화된 작업에서 더 높은 정확도를 달성합니다. 실험 결과, DynamicNER는 LLM 기반 NER 방법에 대한 강력하고 효과적인 벤치마크로 기능합니다. 또한, 우리는 데이터셋에서 전통적인 방법과 LLM 기반 방법에 대한 분석도 수행합니다. 우리의 코드와 데이터셋은 https://github.com/Astarojth/DynamicNER에서 공개적으로 이용 가능합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 개체명 인식(NER) 방법에 대한 연구로, 기존 데이터셋의 한계를 극복하기 위해 DynamicNER라는 새로운 데이터셋을 제안합니다. DynamicNER는 LLM 기반 방법에 적합하도록 동적 범주화를 도입하여 다양한 문맥에서 동일 개체에 대해 여러 유형의 범주를 제공합니다. 이 데이터셋은 8개 언어와 155개 개체 유형을 포함하며, 다양한 도메인을 아우릅니다. 또한, CascadeNER라는 새로운 NER 방법론을 제안하여 경량 LLM을 활용한 두 단계 전략으로 세밀한 작업에서 높은 정확도를 달성하면서도 적은 계산 자원을 요구합니다. 실험 결과, DynamicNER는 LLM 기반 NER 방법의 강력한 벤치마크로 기능하며, 전통적 방법과 LLM 기반 방법 모두에 대한 분석을 수행했습니다.

## 🎯 주요 포인트

- 1. 기존 데이터셋은 LLM 기반의 개체명 인식(NER) 방법에 적합하지 않으며, 이를 해결하기 위해 DynamicNER라는 새로운 데이터셋을 제안합니다.

- 2. DynamicNER는 다양한 문맥에서 동일한 개체에 대해 여러 개체 유형과 목록을 도입하여 LLM 기반 NER의 일반화 능력을 활용합니다.

- 3. 이 데이터셋은 8개 언어와 155개의 개체 유형을 포함하며, 다양한 도메인을 아우르는 다중 언어 및 다중 세분화 특성을 가지고 있습니다.

- 4. CascadeNER라는 새로운 NER 방법은 두 단계 전략과 경량 LLM을 기반으로 하여, 더 적은 계산 자원으로도 세분화된 작업에서 높은 정확도를 달성합니다.

- 5. DynamicNER는 LLM 기반 NER 방법의 강력하고 효과적인 벤치마크로 기능하며, 전통적인 방법과 LLM 기반 방법에 대한 분석도 수행되었습니다.

---

*Generated on 2025-09-22 14:38:14*