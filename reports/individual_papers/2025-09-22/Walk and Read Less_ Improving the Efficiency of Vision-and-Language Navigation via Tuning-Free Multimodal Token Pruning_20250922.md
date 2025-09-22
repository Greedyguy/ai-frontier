# Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning

**Korean Title:** 걷기와 읽기 줄이기: 조정이 필요 없는 다중 모달 토큰 가지치기를 통한 시각-언어 내비게이션의 효율성 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Navigation Specific Traits

## 🔗 유사한 논문
- [[2025-09-17/NIRVANA_ Structured pruning reimagined for large language models compression_20250917|NIRVANA Structured pruning reimagined for large language models compression]] (85.8% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (83.4% similar)
- [[2025-09-19/T-araVLN_ Translator for Agricultural Robotic Agents on Vision-and-Language Navigation_20250919|T-araVLN Translator for Agricultural Robotic Agents on Vision-and-Language Navigation]] (82.4% similar)
- [[2025-09-18/FSR-VLN_ Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph_20250918|FSR-VLN Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (82.0% similar)
- [[2025-09-19/Handle Object Navigation as Weighted Traveling Repairman Problem_20250919|Handle Object Navigation as Weighted Traveling Repairman Problem]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15250v1 Announce Type: cross 
Abstract: Large models achieve strong performance on Vision-and-Language Navigation (VLN) tasks, but are costly to run in resource-limited environments. Token pruning offers appealing tradeoffs for efficiency with minimal performance loss by reducing model input size, but prior work overlooks VLN-specific challenges. For example, information loss from pruning can effectively increase computational cost due to longer walks. Thus, the inability to identify uninformative tokens undermines the supposed efficiency gains from pruning. To address this, we propose Navigation-Aware Pruning (NAP), which uses navigation-specific traits to simplify the pruning process by pre-filtering tokens into foreground and background. For example, image views are filtered based on whether the agent can navigate in that direction. We also extract navigation-relevant instructions using a Large Language Model. After filtering, we focus pruning on background tokens, minimizing information loss. To further help avoid increases in navigation length, we discourage backtracking by removing low-importance navigation nodes. Experiments on standard VLN benchmarks show NAP significantly outperforms prior work, preserving higher success rates while saving more than 50% FLOPS.

## 🔍 Abstract (한글 번역)

arXiv:2509.15250v1 발표 유형: 교차  
초록: 대형 모델은 시각 및 언어 내비게이션(VLN) 과제에서 강력한 성능을 발휘하지만, 자원이 제한된 환경에서는 실행 비용이 많이 듭니다. 토큰 가지치기는 모델 입력 크기를 줄여 성능 손실을 최소화하면서 효율성을 위한 매력적인 절충안을 제공합니다. 그러나 이전 연구는 VLN에 특화된 도전 과제를 간과했습니다. 예를 들어, 가지치기로 인한 정보 손실은 더 긴 경로로 인해 계산 비용을 효과적으로 증가시킬 수 있습니다. 따라서 비정보성 토큰을 식별하지 못하면 가지치기로 인한 효율성 향상이 저해됩니다. 이를 해결하기 위해, 우리는 내비게이션 인식 가지치기(NAP)를 제안합니다. 이는 내비게이션 특화 특성을 사용하여 토큰을 전경과 배경으로 사전 필터링하여 가지치기 과정을 단순화합니다. 예를 들어, 에이전트가 해당 방향으로 이동할 수 있는지 여부에 따라 이미지 뷰가 필터링됩니다. 또한, 대형 언어 모델을 사용하여 내비게이션 관련 지시를 추출합니다. 필터링 후, 우리는 정보 손실을 최소화하기 위해 배경 토큰에 가지치기를 집중합니다. 내비게이션 길이 증가를 피하기 위해, 중요도가 낮은 내비게이션 노드를 제거하여 후퇴를 방지합니다. 표준 VLN 벤치마크에 대한 실험 결과, NAP는 이전 연구보다 유의미하게 뛰어난 성능을 보이며, 성공률을 높게 유지하면서도 50% 이상의 FLOPS를 절약합니다.

## 📝 요약

이 논문은 Vision-and-Language Navigation(VLN) 작업에서 대규모 모델의 효율성을 높이기 위해 제안된 Navigation-Aware Pruning(NAP) 방법론을 소개합니다. 기존의 토큰 프루닝 기법은 정보 손실로 인해 오히려 계산 비용을 증가시킬 수 있는 문제를 가지고 있었습니다. NAP는 내비게이션에 특화된 특성을 활용하여 토큰을 전경과 배경으로 사전 필터링하고, 배경 토큰에 집중하여 정보 손실을 최소화합니다. 또한, 중요도가 낮은 내비게이션 노드를 제거하여 경로 길이 증가를 방지합니다. 실험 결과, NAP는 기존 방법보다 높은 성공률을 유지하면서도 50% 이상의 FLOPS를 절약하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 대형 모델은 Vision-and-Language Navigation (VLN) 작업에서 높은 성능을 보이지만, 자원이 제한된 환경에서는 실행 비용이 높습니다.

- 2. 토큰 프루닝은 모델 입력 크기를 줄여 효율성을 높이는 동시에 성능 손실을 최소화하는 매력적인 방법입니다.

- 3. 기존 연구는 VLN의 특수한 도전 과제를 간과했으며, 정보 손실은 오히려 계산 비용을 증가시킬 수 있습니다.

- 4. Navigation-Aware Pruning (NAP)은 내비게이션 특성을 활용하여 토큰을 전경과 배경으로 사전 필터링하여 프루닝 과정을 단순화합니다.

- 5. NAP는 표준 VLN 벤치마크 실험에서 이전 연구보다 높은 성공률을 유지하면서도 50% 이상의 FLOPS를 절약합니다.

---

*Generated on 2025-09-22 13:49:35*