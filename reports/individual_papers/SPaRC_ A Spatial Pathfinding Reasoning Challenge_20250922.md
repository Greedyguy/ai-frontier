# SPaRC: A Spatial Pathfinding Reasoning Challenge

**Korean Title:** SPaRC: 공간 경로 찾기 추론 도전 과제

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Abstract Multi-step Problem Solving

## 🔗 유사한 논문
- [[2025-09-22/SmolRGPT_ Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters_20250922|SmolRGPT Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters]] (80.7% similar)
- [[2025-09-22/KNARsack_ Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems_20250922|KNARsack Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems]] (80.2% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (79.2% similar)
- [[2025-09-18/The NazoNazo Benchmark_ A Cost-Effective and Extensible Test of Insight-Based Reasoning in LLMs_20250918|The NazoNazo Benchmark A Cost-Effective and Extensible Test of Insight-Based Reasoning in LLMs]] (79.0% similar)
- [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek Training-Free Spatial Prompting for Multimodal Large Language Model]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16686v2 Announce Type: replace 
Abstract: Existing reasoning datasets saturate and fail to test abstract, multi-step problems, especially pathfinding and complex rule constraint satisfaction. We introduce SPaRC (Spatial Pathfinding Reasoning Challenge), a dataset of 1,000 2D grid pathfinding puzzles to evaluate spatial and symbolic reasoning, requiring step-by-step planning with arithmetic and geometric rules. Humans achieve near-perfect accuracy (98.0%; 94.5% on hard puzzles), while the best reasoning models, such as o4-mini, struggle (15.8%; 1.1% on hard puzzles). Models often generate invalid paths (>50% of puzzles for o4-mini), and reasoning tokens reveal they make errors in navigation and spatial logic. Unlike humans, who take longer on hard puzzles, models fail to scale test-time compute with difficulty. Allowing models to make multiple solution attempts improves accuracy, suggesting potential for better spatial reasoning with improved training and efficient test-time scaling methods. SPaRC can be used as a window into models' spatial reasoning limitations and drive research toward new methods that excel in abstract, multi-step problem-solving.

## 🔍 Abstract (한글 번역)

arXiv:2505.16686v2 발표 유형: 교체  
초록: 기존의 추론 데이터셋은 추상적이고 다단계 문제, 특히 경로 찾기와 복잡한 규칙 제약 만족 문제를 테스트하는 데 한계를 보입니다. 우리는 공간적 및 상징적 추론을 평가하기 위해 SPaRC(Spatial Pathfinding Reasoning Challenge)를 소개합니다. 이 데이터셋은 산술 및 기하학적 규칙을 사용한 단계별 계획이 필요한 1,000개의 2D 그리드 경로 찾기 퍼즐로 구성되어 있습니다. 인간은 거의 완벽한 정확도(98.0%; 어려운 퍼즐에서는 94.5%)를 달성하지만, o4-mini와 같은 최고의 추론 모델은 어려움을 겪습니다(15.8%; 어려운 퍼즐에서는 1.1%). 모델은 종종 잘못된 경로를 생성하며(o4-mini의 경우 퍼즐의 50% 이상), 추론 토큰은 모델이 탐색 및 공간 논리에서 오류를 범함을 드러냅니다. 인간과 달리, 어려운 퍼즐에서 더 많은 시간이 소요되는 반면, 모델은 난이도에 따라 테스트 시간 계산을 확장하지 못합니다. 모델이 여러 번의 해결 시도를 할 수 있도록 하면 정확도가 향상되며, 이는 개선된 훈련과 효율적인 테스트 시간 확장 방법을 통해 더 나은 공간 추론의 가능성을 시사합니다. SPaRC는 모델의 공간 추론 한계를 이해하고, 추상적이고 다단계 문제 해결에 뛰어난 새로운 방법을 연구하는 데 기여할 수 있습니다.

## 📝 요약

SPaRC(Spatial Pathfinding Reasoning Challenge)는 2D 그리드 경로 찾기 퍼즐 1,000개로 구성된 데이터셋으로, 공간적 및 상징적 추론을 평가합니다. 이 데이터셋은 산술 및 기하학적 규칙을 활용한 단계별 계획이 필요합니다. 인간은 거의 완벽한 정확도(98.0%; 어려운 퍼즐에서 94.5%)를 보이는 반면, 최상의 추론 모델인 o4-mini는 낮은 성능(15.8%; 어려운 퍼즐에서 1.1%)을 보입니다. 모델은 종종 잘못된 경로를 생성하며, 탐색 및 공간 논리에서 오류를 범합니다. 모델은 난이도에 따라 테스트 시간 계산을 조정하지 못하지만, 여러 번의 시도를 허용하면 정확도가 향상됩니다. SPaRC는 모델의 공간 추론 한계를 이해하고, 추상적이고 다단계 문제 해결에 뛰어난 새로운 방법 개발을 촉진할 수 있습니다.

## 🎯 주요 포인트

- 1. SPaRC는 2D 그리드 경로 찾기 퍼즐을 통해 공간적 및 상징적 추론을 평가하는 데이터셋입니다.

- 2. 인간은 SPaRC 퍼즐에서 거의 완벽한 정확도를 보이지만, 최상의 추론 모델은 낮은 성과를 보입니다.

- 3. 모델들은 경로 생성 시 많은 오류를 범하며, 특히 어려운 퍼즐에서 테스트 시간 계산을 확장하지 못합니다.

- 4. 모델이 여러 번의 해결 시도를 허용하면 정확도가 향상되며, 이는 향상된 훈련 및 효율적인 테스트 시간 확장 방법의 가능성을 시사합니다.

- 5. SPaRC는 모델의 공간적 추론 한계를 파악하고 추상적이며 다단계 문제 해결에 뛰어난 새로운 방법 연구를 촉진할 수 있습니다.

---

*Generated on 2025-09-22 14:31:36*