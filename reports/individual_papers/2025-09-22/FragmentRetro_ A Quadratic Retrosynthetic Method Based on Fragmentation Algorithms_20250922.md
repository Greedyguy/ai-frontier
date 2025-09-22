# FragmentRetro: A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms

**Korean Title:** FragmentRetro: 분해 알고리즘에 기반한 이차적 역합성 방법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Stock Aware Exploration

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (77.2% similar)
- [[2025-09-18/Position Bias Mitigates Position Bias_Mitigate Position Bias Through Inter-Position Knowledge Distillation_20250918|Position Bias Mitigates Position BiasMitigate Position Bias Through Inter-Position Knowledge Distillation]] (76.3% similar)
- [[2025-09-19/jXBW_ Fast Substructure Search for Large-Scale JSONL Datasets with LLM Applications_20250919|jXBW Fast Substructure Search for Large-Scale JSONL Datasets with LLM Applications]] (76.0% similar)
- [[2025-09-17/Where Do Tokens Go Understanding Pruning Behaviors in STEP at High Resolutions_20250917|Where Do Tokens Go Understanding Pruning Behaviors in STEP at High Resolutions]] (75.8% similar)
- [[2025-09-19/Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (75.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15409v1 Announce Type: new 
Abstract: Retrosynthesis, the process of deconstructing a target molecule into simpler precursors, is crucial for computer-aided synthesis planning (CASP). Widely adopted tree-search methods often suffer from exponential computational complexity. In this work, we introduce FragmentRetro, a novel retrosynthetic method that leverages fragmentation algorithms, specifically BRICS and r-BRICS, combined with stock-aware exploration and pattern fingerprint screening to achieve quadratic complexity. FragmentRetro recursively combines molecular fragments and verifies their presence in a building block set, providing sets of fragment combinations as retrosynthetic solutions. We present the first formal computational analysis of retrosynthetic methods, showing that tree search exhibits exponential complexity $O(b^h)$, DirectMultiStep scales as $O(h^6)$, and FragmentRetro achieves $O(h^2)$, where $h$ represents the number of heavy atoms in the target molecule and $b$ is the branching factor for tree search. Evaluations on PaRoutes, USPTO-190, and natural products demonstrate that FragmentRetro achieves high solved rates with competitive runtime, including cases where tree search fails. The method benefits from fingerprint screening, which significantly reduces substructure matching complexity. While FragmentRetro focuses on efficiently identifying fragment-based solutions rather than full reaction pathways, its computational advantages and ability to generate strategic starting candidates establish it as a powerful foundational component for scalable and automated synthesis planning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15409v1 발표 유형: 신규  
초록: 레트로신테시스는 목표 분자를 더 간단한 전구체로 분해하는 과정으로, 컴퓨터 지원 합성 계획(CASP)에 필수적입니다. 널리 채택된 트리 탐색 방법은 종종 지수적 계산 복잡성의 문제를 겪습니다. 본 연구에서는 BRICS와 r-BRICS라는 분할 알고리즘을 활용하고, 재고 인식 탐색 및 패턴 지문 스크리닝을 결합하여 이차 복잡성을 달성하는 새로운 레트로신테시스 방법인 FragmentRetro를 소개합니다. FragmentRetro는 분자 조각을 재귀적으로 결합하고, 이들이 빌딩 블록 세트에 존재하는지를 확인하여 레트로신테시스 솔루션으로 조각 조합 세트를 제공합니다. 우리는 레트로신테시스 방법에 대한 최초의 공식적인 계산 분석을 제시하며, 트리 탐색이 지수적 복잡성 $O(b^h)$를 나타내고, DirectMultiStep이 $O(h^6)$로 확장되며, FragmentRetro가 $O(h^2)$를 달성함을 보여줍니다. 여기서 $h$는 목표 분자의 무거운 원자 수를 나타내고, $b$는 트리 탐색의 분기 계수입니다. PaRoutes, USPTO-190 및 천연물에 대한 평가 결과, FragmentRetro는 트리 탐색이 실패하는 경우를 포함하여 경쟁력 있는 실행 시간과 높은 해결률을 달성함을 보여줍니다. 이 방법은 지문 스크리닝의 이점을 받아 하부 구조 매칭 복잡성을 크게 줄입니다. FragmentRetro는 전체 반응 경로보다는 조각 기반 솔루션을 효율적으로 식별하는 데 중점을 두지만, 그 계산적 이점과 전략적 시작 후보를 생성하는 능력은 확장 가능하고 자동화된 합성 계획을 위한 강력한 기초 구성 요소로 자리 잡습니다.

## 📝 요약

이 논문은 새로운 레트로 합성 방법인 FragmentRetro를 소개합니다. 이 방법은 BRICS와 r-BRICS 분할 알고리즘을 활용하여 분자 조각을 결합하고, 재고 인식 탐색 및 패턴 지문 스크리닝을 통해 이차 복잡성을 달성합니다. FragmentRetro는 분자 조각을 재귀적으로 결합하고, 이를 빌딩 블록 세트에서 확인하여 레트로 합성 솔루션을 제공합니다. 기존의 트리 탐색 방법이 지수적 복잡성을 가지는 반면, FragmentRetro는 $O(h^2)$의 복잡성을 달성합니다. PaRoutes, USPTO-190 및 천연물에 대한 평가에서 높은 해결률과 경쟁력 있는 실행 시간을 보여주며, 트리 탐색이 실패하는 경우에도 효과적입니다. 이 방법은 전체 반응 경로보다는 조각 기반 솔루션을 효율적으로 식별하는 데 중점을 두며, 대규모 자동 합성 계획의 강력한 기초 요소로 자리 잡습니다.

## 🎯 주요 포인트

- 1. FragmentRetro는 BRICS 및 r-BRICS 분할 알고리즘을 활용하여 이차 복잡성을 달성하는 새로운 레트로신테틱 방법입니다.

- 2. FragmentRetro는 분자 조각을 재귀적으로 결합하고 이를 빌딩 블록 세트에서 확인하여 레트로신테틱 솔루션을 제공합니다.

- 3. FragmentRetro는 트리 검색의 지수 복잡성을 피하고, $O(h^2)$의 복잡성을 달성하여 효율성을 높입니다.

- 4. PaRoutes, USPTO-190, 천연물 평가에서 FragmentRetro는 높은 해결률과 경쟁력 있는 실행 시간을 보여줍니다.

- 5. FragmentRetro는 전체 반응 경로보다는 조각 기반 솔루션 식별에 중점을 두며, 자동화된 합성 계획의 강력한 기초 구성 요소로 자리 잡습니다.

---

*Generated on 2025-09-22 13:44:05*