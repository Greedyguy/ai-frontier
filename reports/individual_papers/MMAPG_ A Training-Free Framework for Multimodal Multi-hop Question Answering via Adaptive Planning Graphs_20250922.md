# MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs

**Korean Title:** MMAPG: 적응형 계획 그래프를 통한 다중 모달 다중 홉 질문 응답을 위한 훈련이 필요 없는 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Training-Free Framework

## 🔗 유사한 논문
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (84.0% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (82.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (82.4% similar)
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA Multi-modal Objects-aware Cross-arcHitecture Alignment]] (82.2% similar)
- [[2025-09-19/TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (82.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.16051v2 Announce Type: replace 
Abstract: Multimodal Multi-hop question answering requires integrating information from diverse sources, such as images and texts, to derive answers. Existing methods typically rely on sequential retrieval and reasoning, where each step builds on the previous output. However, this single-path paradigm makes them vulnerable to errors due to misleading intermediate steps. Moreover, developing multimodal models can be computationally expensive, often requiring extensive training. To address these limitations, we propose a training-free framework guided by an Adaptive Planning Graph, which consists of planning, retrieval and reasoning modules. The planning module analyzes the current state of the Adaptive Planning Graph, determines the next action and where to expand the graph, which enables dynamic and flexible exploration of reasoning paths. To handle retrieval of text to unspecified target modalities, we devise modality-specific strategies that dynamically adapt to distinct data types. Our approach preserves the characteristics of multimodal information without costly task-specific training, enabling seamless integration with up-to-date models. Finally, the experiments on MultimodalQA and WebQA show that our approach matches or outperforms existing models that rely on training.

## 🔍 Abstract (한글 번역)

arXiv:2508.16051v2 발표 유형: 교체  
초록: 다중모달 다중단계 질문 응답은 이미지와 텍스트와 같은 다양한 출처에서 정보를 통합하여 답을 도출해야 합니다. 기존 방법들은 일반적으로 순차적 검색과 추론에 의존하며, 각 단계는 이전 출력에 기반을 둡니다. 그러나 이 단일 경로 패러다임은 중간 단계의 오류로 인해 오답에 취약하게 만듭니다. 게다가, 다중모달 모델 개발은 종종 광범위한 훈련을 필요로 하여 계산 비용이 많이 들 수 있습니다. 이러한 제한점을 해결하기 위해, 우리는 계획, 검색, 추론 모듈로 구성된 적응형 계획 그래프에 의해 안내되는 훈련이 필요 없는 프레임워크를 제안합니다. 계획 모듈은 적응형 계획 그래프의 현재 상태를 분석하고, 다음 행동과 그래프를 확장할 위치를 결정하여 추론 경로의 동적이고 유연한 탐색을 가능하게 합니다. 명시되지 않은 대상 모달리티로의 텍스트 검색을 처리하기 위해, 우리는 서로 다른 데이터 유형에 동적으로 적응하는 모달리티별 전략을 고안했습니다. 우리의 접근 방식은 비용이 많이 드는 작업별 훈련 없이 다중모달 정보의 특성을 유지하며, 최신 모델과의 원활한 통합을 가능하게 합니다. 마지막으로, MultimodalQA와 WebQA에 대한 실험 결과, 우리의 접근 방식이 훈련에 의존하는 기존 모델과 동등하거나 더 우수한 성능을 보임을 확인했습니다.

## 📝 요약

이 논문은 멀티모달 멀티홉 질문 응답 문제를 해결하기 위해 새로운 접근 방식을 제안합니다. 기존 방법들은 순차적인 검색과 추론에 의존하여 중간 단계에서의 오류에 취약하고, 멀티모달 모델 개발에 많은 비용이 듭니다. 이를 해결하기 위해, 저자들은 Adaptive Planning Graph를 기반으로 한 훈련이 필요 없는 프레임워크를 제안합니다. 이 프레임워크는 계획, 검색, 추론 모듈로 구성되어 있으며, 동적이고 유연한 추론 경로 탐색을 가능하게 합니다. 또한, 텍스트 검색을 위한 모달리티별 전략을 도입하여 다양한 데이터 유형에 적응합니다. 실험 결과, 제안된 방법은 MultimodalQA와 WebQA에서 기존 모델과 동등하거나 더 나은 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 멀티모달 멀티홉 질문 응답은 이미지와 텍스트 등 다양한 소스의 정보를 통합하여 답을 도출해야 합니다.

- 2. 기존 방법은 순차적 검색 및 추론에 의존하여 중간 단계의 오류에 취약합니다.

- 3. 제안된 프레임워크는 Adaptive Planning Graph를 활용하여 훈련 없이 계획, 검색, 추론 모듈을 통해 동적이고 유연한 추론 경로 탐색을 가능하게 합니다.

- 4. 텍스트 검색을 위해 모달리티별 전략을 사용하여 다양한 데이터 유형에 동적으로 적응합니다.

- 5. MultimodalQA와 WebQA 실험에서 제안된 방법이 기존 훈련 기반 모델과 동등하거나 더 나은 성능을 보였습니다.

---

*Generated on 2025-09-22 14:33:28*