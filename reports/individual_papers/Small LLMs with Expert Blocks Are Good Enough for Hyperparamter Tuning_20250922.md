# Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning

**Korean Title:** 전문 블록을 포함한 작은 LLM은 하이퍼파라미터 튜닝에 충분하다

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Trajectory Context Summarizer

## 🔗 유사한 논문
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (85.4% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (83.5% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (83.2% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (83.1% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (83.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15561v1 Announce Type: new 
Abstract: Hyper-parameter Tuning (HPT) is a necessary step in machine learning (ML) pipelines but becomes computationally expensive and opaque with larger models. Recently, Large Language Models (LLMs) have been explored for HPT, yet most rely on models exceeding 100 billion parameters. We propose an Expert Block Framework for HPT using Small LLMs. At its core is the Trajectory Context Summarizer (TCS), a deterministic block that transforms raw training trajectories into structured context, enabling small LLMs to analyze optimization progress with reliability comparable to larger models. Using two locally-run LLMs (phi4:reasoning14B and qwen2.5-coder:32B) and a 10-trial budget, our TCS-enabled HPT pipeline achieves average performance within ~0.9 percentage points of GPT-4 across six diverse tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15561v1 발표 유형: 신규  
초록: 하이퍼파라미터 튜닝(HPT)은 머신러닝(ML) 파이프라인에서 필수적인 단계이지만, 모델이 커질수록 계산 비용이 많이 들고 불투명해집니다. 최근 대형 언어 모델(LLM)이 HPT에 탐구되고 있지만, 대부분은 1,000억 개 이상의 파라미터를 가진 모델에 의존합니다. 우리는 소형 LLM을 사용한 HPT를 위한 전문가 블록 프레임워크를 제안합니다. 그 핵심은 Trajectory Context Summarizer(TCS)로, 원시 훈련 경로를 구조화된 컨텍스트로 변환하는 결정론적 블록입니다. 이를 통해 소형 LLM이 더 큰 모델과 비교할 수 있는 신뢰성으로 최적화 진행을 분석할 수 있습니다. 두 개의 로컬 실행 LLM(phi4:reasoning14B 및 qwen2.5-coder:32B)과 10회 실험 예산을 사용하여, TCS를 활용한 HPT 파이프라인은 여섯 가지 다양한 작업에서 GPT-4와 평균 성능 차이가 약 0.9 퍼센트 포인트 이내로 달성되었습니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)을 사용하지 않고도 효과적인 하이퍼파라미터 튜닝(HPT)을 수행할 수 있는 방법을 제안합니다. 제안된 방법은 '전문가 블록 프레임워크'로, 핵심 구성 요소인 'Trajectory Context Summarizer(TCS)'를 통해 작은 LLM이 대규모 모델과 유사한 신뢰도로 최적화 진행 상황을 분석할 수 있게 합니다. 두 개의 소규모 LLM(phi4:reasoning14B 및 qwen2.5-coder:32B)을 사용하여 10번의 실험 예산 내에서 GPT-4와 비교해 평균 성능 차이가 약 0.9% 포인트에 불과한 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 하이퍼파라미터 튜닝(HPT)은 머신러닝 파이프라인에서 필수적이지만, 대형 모델에서는 계산 비용이 많이 들고 불투명해진다.

- 2. 소형 대형 언어 모델(LLMs)을 활용한 전문가 블록 프레임워크를 제안하여 HPT를 수행한다.

- 3. Trajectory Context Summarizer(TCS)는 훈련 경로를 구조화된 컨텍스트로 변환하여 소형 LLM이 최적화 진행을 분석할 수 있도록 한다.

- 4. 두 개의 로컬 LLM(phi4:reasoning14B 및 qwen2.5-coder:32B)을 사용하여, 10번의 시도 예산 내에서 GPT-4와 유사한 성능을 달성하였다.

- 5. 제안된 HPT 파이프라인은 여섯 가지 다양한 작업에서 평균 성능이 GPT-4와 약 0.9 퍼센트 포인트 차이를 보인다.

---

*Generated on 2025-09-22 15:20:02*