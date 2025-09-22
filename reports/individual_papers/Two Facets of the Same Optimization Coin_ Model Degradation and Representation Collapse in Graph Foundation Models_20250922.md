# Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models

**Korean Title:** 동일한 최적화 코인의 두 가지 측면: 그래프 기초 모델에서의 모델 열화와 표현 붕괴

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Edge-wise Semantic Fusion|Edge-wise Semantic Fusion]] [[keywords/specific/Domain Generalization|Domain Generalization]] [[keywords/specific/Graph VQ MAE|Graph VQ MAE]] [[keywords/broad/Graph Foundation Models|Graph Foundation Models]] [[keywords/unique/MoT|MoT]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (82.8% similar) [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.6% similar) [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Edge-wise Semantic Fusion
**🔗 Specific Connectable**: Domain Generalization
**🔬 Broad Technical**: Graph Foundation Models
**⭐ Unique Technical**: MoT
## 🔗 유사한 논문
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (82.8% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.6% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization From Traditional Approaches to Foundation Models]] (82.3% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.8% similar)
- [[2025-09-17/Class-invariant Test-Time Augmentation for Domain Generalization_20250917|Class-invariant Test-Time Augmentation for Domain Generalization]] (81.5% similar)


**ArXiv ID**: [2509.08401](https://arxiv.org/abs/2509.08401)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.08401.pdf)


**ArXiv ID**: [2509.08401](https://arxiv.org/abs/2509.08401)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.08401.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Discrete Embedding Spaces
**🔗 Specific Connectable**: Domain Generalization, Semantic Fusion
**⭐ Unique Technical**: MoT
**🔬 Broad Technical**: Graph Foundation Models

## 🏷️ 추출된 키워드



`Graph Foundation Models` • 

`Domain Generalization` • 

`Graph Neural Network` • 

`Graph VQ-MAE` • 

`MoT`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08401v4 Announce Type: replace 
Abstract: Inspired by the success of LLMs, GFMs are designed to learn the optimal embedding functions from multi-domain text-attributed graphs for the downstream cross-task generalization capability. Among the diverse architectures, graph VQ-MAE stands out among the increasingly diverse landscape of GFM. This is attributed to its ability to jointly encode topology and textual attributes from multiple domains into discrete embedding spaces with clear semantic boundaries. Despite its potential, domain generalization conflicts cause imperceptible pitfalls. In this paper, we instantiate two of them, and they are just like two sides of the same GFM optimization coin - Side 1 Model Degradation: The encoder and codebook fail to capture the diversity of inputs; Side 2 Representation Collapse: The hidden embedding and codebook vector fail to preserve semantic separability due to constraints from narrow representation subspaces. These two pitfalls (sides) collectively impair the decoder and generate the low-quality reconstructed supervision, causing the GFM optimization dilemma during pre-training (coin). Through empirical investigation, we attribute the above challenges to Information Bottleneck and Regularization Deficit. To address them, we propose MoT - (1) Information Tinker for Two Pitfalls, which utilizes an edge-wise semantic fusion strategy and a mixture-of-codebooks with domain-aware routing to improve information capacity. (2) Regularization Tinker for Optimization Coin, which utilizes two additional regularizations to further improve gradient supervision in our proposed Information Tinker. Notably, as a flexible architecture, MoT adheres to the scaling laws of GFM, offering a controllable model scale. Compared to SOTA baselines, experiments on 22 datasets across 6 domains demonstrate that MoT achieves significant improvements in supervised, few-shot, and zero-shot scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.08401v4 발표 유형: 교체  
초록: LLM의 성공에 영감을 받아, GFM은 다중 도메인 텍스트 속성 그래프로부터 최적의 임베딩 함수를 학습하여 다운스트림 크로스 태스크 일반화 능력을 갖추도록 설계되었습니다. 다양한 아키텍처 중에서, 그래프 VQ-MAE는 GFM의 점점 더 다양해지는 환경에서 두드러집니다. 이는 여러 도메인의 토폴로지와 텍스트 속성을 명확한 의미 경계를 가진 이산 임베딩 공간으로 함께 인코딩할 수 있는 능력에 기인합니다. 그 잠재력에도 불구하고, 도메인 일반화 충돌은 미세한 함정을 초래합니다. 이 논문에서는 두 가지를 구체화하며, 이는 GFM 최적화의 양면과 같습니다 - 측면 1 모델 열화: 인코더와 코드북이 입력의 다양성을 포착하지 못함; 측면 2 표현 붕괴: 숨겨진 임베딩과 코드북 벡터가 좁은 표현 하위 공간의 제약으로 인해 의미적 분리성을 유지하지 못함. 이 두 가지 함정(측면)은 디코더를 집합적으로 손상시키고 저품질의 재구성된 감독을 생성하여 사전 학습 중 GFM 최적화 딜레마(동전)를 초래합니다. 경험적 조사를 통해, 우리는 위의 문제를 정보 병목 현상과 정규화 결핍에 기인한다고 봅니다. 이를 해결하기 위해, 우리는 MoT를 제안합니다 - (1) 두 가지 함정을 위한 정보 조정, 이는 엣지 기반 의미 융합 전략과 도메인 인식 라우팅을 갖춘 코드북 혼합을 활용하여 정보 용량을 향상시킵니다. (2) 최적화 동전을 위한 정규화 조정, 이는 제안된 정보 조정에서 그래디언트 감독을 더욱 향상시키기 위해 두 가지 추가 정규화를 활용합니다. 특히, 유연한 아키텍처로서 MoT는 GFM의 스케일링 법칙을 준수하여 제어 가능한 모델 규모를 제공합니다. SOTA 기준선과 비교하여, 6개 도메인에 걸친 22개의 데이터셋에서의 실험은 MoT가 감독, 소수 샷, 제로 샷 시나리오에서 상당한 개선을 달성함을 보여줍니다.

## 📝 요약

이 논문은 LLM의 성공에 영감을 받아, 다중 도메인 텍스트 속성 그래프에서 최적의 임베딩 함수를 학습하여 다양한 작업에 일반화할 수 있는 GFM을 설계합니다. 특히, 그래프 VQ-MAE는 여러 도메인의 토폴로지와 텍스트 속성을 명확한 의미 경계를 가진 이산 임베딩 공간으로 인코딩하는 능력으로 주목받습니다. 그러나 도메인 일반화의 문제로 인해 모델 열화와 표현 붕괴라는 두 가지 문제가 발생합니다. 이를 해결하기 위해 정보 병목 현상과 규제 부족을 원인으로 지목하고, MoT를 제안합니다. MoT는 두 가지 문제를 해결하기 위한 정보 조정 전략과 최적화 문제를 해결하기 위한 추가 규제를 포함합니다. 실험 결과, MoT는 6개 도메인 22개 데이터셋에서 기존 모델 대비 유의미한 성능 향상을 보였습니다.

## 🎯 주요 포인트


- 1. Graph VQ-MAE는 다중 도메인의 텍스트 속성을 명확한 의미 경계를 가진 이산 임베딩 공간으로 인코딩하는 능력으로 주목받고 있습니다.

- 2. 도메인 일반화의 한계로 인해 모델 열화와 표현 붕괴라는 두 가지 문제가 발생하며, 이는 GFM 최적화 딜레마를 초래합니다.

- 3. 정보 병목 현상과 정규화 부족이 이러한 문제의 원인으로 지목되며, 이를 해결하기 위해 MoT를 제안합니다.

- 4. MoT는 정보 용량을 개선하기 위한 엣지 기반 의미 융합 전략과 도메인 인식 라우팅을 활용한 코드북 혼합을 포함합니다.

- 5. MoT는 6개 도메인에 걸친 22개의 데이터셋에서 SOTA 기준을 초과하는 성능을 보이며, 유연한 아키텍처로서 GFM의 확장 법칙을 따릅니다.


---

*Generated on 2025-09-22 16:03:24*