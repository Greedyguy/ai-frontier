
# NIRVANA: Structured pruning reimagined for large language models compression

**Korean Title:** NIRVANA: 대형 언어 모델 압축을 위해 재구성된 구조화된 가지치기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Zero-shot settings|Zero-shot settings]] [[keywords/broad/Structured pruning|Structured pruning]] [[keywords/broad/Large language models|Large language models]] [[keywords/specific/Neural Tangent Kernel|Neural Tangent Kernel]] [[keywords/unique/NIRVANA|NIRVANA]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive sparsity allocation
**🔬 Broad Technical**: Structured pruning, Large language models
**🔗 Specific Connectable**: Neural Tangent Kernel
**⭐ Unique Technical**: NIRVANA

**ArXiv ID**: [2509.14230](https://arxiv.org/abs/2509.14230)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.14230.pdf)


## 🏷️ 추출된 키워드



`Structured pruning` • 

`Large language models` • 

`Neural Tangent Kernel` • 

`NIRVANA` • 

`Adaptive sparsity allocation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14230v1 Announce Type: new 
Abstract: Structured pruning of large language models (LLMs) offers substantial efficiency improvements by removing entire hidden units, yet current approaches often suffer from significant performance degradation, particularly in zero-shot settings, and necessitate costly recovery techniques such as supervised fine-tuning (SFT) or adapter insertion. To address these critical shortcomings, we introduce NIRVANA, a novel pruning method explicitly designed to balance immediate zero-shot accuracy preservation with robust fine-tuning capability. Leveraging a first-order saliency criterion derived from the Neural Tangent Kernel under Adam optimization dynamics, NIRVANA provides a theoretically grounded pruning strategy that respects essential model training behaviors. To further address the unique challenges posed by structured pruning, NIRVANA incorporates an adaptive sparsity allocation mechanism across layers and modules (attention vs. MLP), which adjusts pruning intensity between modules in a globally balanced manner. Additionally, to mitigate the high sensitivity of pruning decisions to calibration data quality, we propose a simple yet effective KL divergence-based calibration data selection strategy, ensuring more reliable and task-agnostic pruning outcomes. Comprehensive experiments conducted on Llama3, Qwen, and T5 models demonstrate that NIRVANA outperforms existing structured pruning methods under equivalent sparsity constraints, providing a theoretically sound and practical approach to LLM compression. The code is available at https://github.com/iDEA-iSAIL-Lab-UIUC/NIRVANA.

## 🔍 Abstract (한글 번역)

arXiv:2509.14230v1 발표 유형: 새로운
요약: 대규모 언어 모델 (LLMs)의 구조화된 가지치기는 전체 숨겨진 단위를 제거함으로써 상당한 효율성 향상을 제공하지만, 현재 접근 방식은 종종 중요한 성능 저하를 겪고 특히 제로샷 설정에서는 고통을 겪고 있으며, 지도된 세밀 조정 (SFT) 또는 어댑터 삽입과 같은 비용이 많이 드는 회복 기술이 필요합니다. 이러한 중요한 결점을 해결하기 위해, 우리는 NIRVANA를 소개합니다. 이는 즉각적인 제로샷 정확도 보존과 견고한 세밀 조정 능력을 균형 있게 유지하도록 명시적으로 설계된 혁신적인 가지치기 방법입니다. Adam 최적화 역학에서 유도된 Neural Tangent Kernel에서 파생된 1차적인 중요도 기준을 활용하여, NIRVANA는 필수적인 모델 훈련 행동을 존중하는 이론적으로 기초가 있는 가지치기 전략을 제공합니다. 구조화된 가지치기가 제기하는 독특한 도전에 대응하기 위해, NIRVANA는 층과 모듈 (어텐션 대 MLP) 간의 가지치기 강도를 전역적으로 균형 있게 조정하는 적응형 희소성 할당 메커니즘을 통합합니다. 또한, 가지치기 결정이 보정 데이터 품질에 대해 높은 민감도를 가질 때, 우리는 간단하면서도 효과적인 KL 발산 기반의 보정 데이터 선택 전략을 제안하여, 더 신뢰할 수 있고 작업에 중립적인 가지치기 결과를 보장합니다. Llama3, Qwen, T5 모델에서 수행된 포괄적인 실험은 NIRVANA가 동등한 희소성 제약 조건 하에서 기존의 구조화된 가지치기 방법을 능가하며, LLM 압축에 대한 이론적으로 탄탄하고 실용적인 접근 방식을 제공함을 보여줍니다. 코드는 https://github.com/iDEA-iSAIL-Lab-UIUC/NIRVANA에서 사용할 수 있습니다.

## 📝 요약

초대형 언어 모델의 구조화된 가지치기는 전체 은닑 유닛을 제거함으로써 상당한 효율 향상을 제공하지만, 현재의 방법은 종종 제로샷 설정에서 중요한 성능 저하를 겪고 있으며, 지도 미세 조정 또는 어댑터 삽입과 같은 비용이 많이 드는 회복 기술이 필요합니다. 이러한 중요한 결점을 해결하기 위해, 우리는 NIRVANA를 소개합니다. NIRVANA는 즉시 제로샷 정확도 보존과 견고한 미세 조정 능력을 균형 있게 유지하도록 명시적으로 설계된 새로운 가지치기 방법입니다. NIRVANA는 Adam 최적화 역학에서 유도된 Neural Tangent Kernel로부터 파생된 1차적인 현저성 기준을 활용하여, 중요한 모델 훈련 행동을 존중하는 이론적으로 기반을 둔 가지치기 전략을 제공합니다. 또한, 구조화된 가지치기가 제기하는 독특한 도전에 대응하기 위해, NIRVANA는 계층 및 모듈 (어텐션 대 MLP) 간의 가지치기 강도를 전역적으로 균형 있게 조정하는 적응형 희소도 할당 메커니즘을 통합합니다. 또한, 가지치기 결정이 보정 데이터 품질에 대한 높은 민감성을 완화하기 위해, KL 발산 기반 보정 데이터 선택 전략을 제안하여 더 신뢰할 수 있고 작업에 중립적인 가지치기 결과를 보장합니다. Llama3, Qwen, T5 모델에서 수행된 포괄적인 실험은 NIRVANA가 동등한 희소 제약 조건 하에서 기존의 구조화된 가지치기 방법을 능가함을 보여주며, LLM 압축에 대한 이론적으로 탄탄하고 실용적인 접근 방식을 제공합니다. 코드는 https://github.com/iDEA-iSAIL-Lab-UIUC/NIRVANA에서 사용할 수 있습니다.

## 🎯 주요 포인트


- 대형 언어 모델의 구조화된 가지치기는 전체 숨겨진 단위를 제거함으로써 상당한 효율성 향상을 제공한다.

- NIRVANA는 즉각적인 제로샷 정확도 보존과 견고한 파인튜닝 능력을 균형 있게 제공하기 위해 설계된 새로운 가지치기 방법을 소개한다.

- NIRVANA은 Adam 최적화 역학에서 유도된 Neural Tangent Kernel에 기초한 1차 순위 중요도 기준을 활용하여 이론적으로 근거 있는 가지치기 전략을 제공한다.


---

*Generated on 2025-09-18 16:40:26*