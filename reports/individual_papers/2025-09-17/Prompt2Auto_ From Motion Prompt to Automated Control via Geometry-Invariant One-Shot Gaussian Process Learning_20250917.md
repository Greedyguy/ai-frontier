---
keywords:
  - Multi-Modal Learning
  - Reinforcement Learning
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:47:46.187193",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Reinforcement Learning",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.79,
    "Reinforcement Learning": 0.78,
    "Few-Shot Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Prompt2Auto: From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning

**Korean Title:** 프롬프트2오토: 운동 프롬프트로부터 기하학 불변 원샷 가우시안 프로세스 학습을 통한 자동화된 제어Maintain the academic tone and technical terminology appropriately.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|learning from demonstration]], [[keywords/Few-Shot Learning|geometry-invariant one-shot Gaussian process]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|multi-skill autonomy]]

## 🔗 유사한 논문
- [[GWM Towards Scalable Gaussian World Models for Robotic Manipulation]] (80.4% similar)
- [[Learning Multimodal Attention for Manipulating Deformable Objects with Changing States]] (79.5% similar)
- [[Humanoid_Agent_via_Embodied_Chain-of-Action_Reasoning_with_Multimodal_Foundation_Models_for_Zero-Shot_Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (79.4% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (79.0% similar)
- [[MAP End-to-End Autonomous Driving with Map-Assisted Planning]] (78.8% similar)

## 📋 저자 정보

**Authors:** Zewen Yang, Xiaobing Dai, Dongfa Zhang, Yu Li, Ziyang Meng, Bingkun Huang, Hamid Sadeghian, Sami Haddadin

## 📄 Abstract (원문)

Learning from demonstration allows robots to acquire complex skills from
human demonstrations, but conventional approaches often require large datasets
and fail to generalize across coordinate transformations. In this paper, we
propose Prompt2Auto, a geometry-invariant one-shot Gaussian process (GeoGP)
learning framework that enables robots to perform human-guided automated
control from a single motion prompt. A dataset-construction strategy based on
coordinate transformations is introduced that enforces invariance to
translation, rotation, and scaling, while supporting multi-step predictions.
Moreover, GeoGP is robust to variations in the user's motion prompt and
supports multi-skill autonomy. We validate the proposed approach through
numerical simulations with the designed user graphical interface and two
real-world robotic experiments, which demonstrate that the proposed method is
effective, generalizes across tasks, and significantly reduces the
demonstration burden. Project page is available at:
https://prompt2auto.github.io

## 🔍 Abstract (한글 번역)

시범 학습을 통해 로봇은 인간의 시범을 통해 복잡한 기술을 습득할 수 있지만, 기존의 방법론은 종종 큰 데이터셋을 필요로 하며 좌표 변환을 통해 일반화하는 데 실패합니다. 본 논문에서는 로봇이 단일 동작 프롬프트로부터 인간 지도 자동 제어를 수행할 수 있도록 하는 geometry-invariant one-shot Gaussian process (GeoGP) 학습 프레임워크인 Prompt2Auto를 제안합니다. 좌표 변환을 기반으로 한 데이터셋 구축 전략이 소개되어 이동, 회전 및 스케일링에 대한 불변성을 강제하면서 다단계 예측을 지원합니다. 또한, GeoGP는 사용자의 동작 프롬프트 변화에 강하며 다중 기술 자율성을 지원합니다. 우리는 제안된 방법론을 설계된 사용자 그래픽 인터페이스와 두 가지 실제 로봇 실험을 통해 수치 시뮬레이션을 통해 검증하였으며, 제안된 방법이 효과적이고 작업 간에 일반화되며 시범 부담을 크게 줄인다는 것을 입증하였습니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://prompt2auto.github.io

## 📝 요약

로봇이 인간의 데모로부터 복잡한 기술을 습득하는 학습은 대규모 데이터셋을 필요로 하고 좌표 변환에 대해 일반화하지 못하는 문제가 있다. 본 논문에서는 Prompt2Auto라는 geometry-invariant one-shot Gaussian process (GeoGP) 학습 프레임워크를 제안한다. 이는 로봇이 단일 동작 프롬프트로부터 인간 지도 아래 자동 제어를 수행할 수 있게 한다. 좌표 변환에 기반한 데이터셋 구축 전략을 소개하여 번역, 회전, 스케일링에 대한 불변성을 강화하고 다단계 예측을 지원한다. 또한, GeoGP는 사용자의 동작 프롬프트 변화에 강건하며 다중 기술 자율성을 지원한다. 제안된 방법을 수치 시뮬레이션과 두 가지 실제 로봇 실험을 통해 검증하여 효과적이며 작업 간에 일반화되며 데모 부담을 크게 줄인다는 것을 입증하였다. 프로젝트 페이지: https://prompt2auto.github.io

## 🎯 주요 포인트

- 로봇이 한국의 지도에서 복잡한 기술을 습득할 수 있도록 하는 학습 방법을 제안합니다.

- 한 번의 동작 프롬프트로 로봇이 인간 지도에 따라 자동 제어할 수 있는 학습 프레임워크를 제안합니다.

- GeoGP는 변환에 불변한 데이터 집합 구축 전략을 도입하여 다양한 예측을 지원합니다.

- GeoGP는 사용자의 동작 프롬프트 변화에 강하며 다중 기술 자율성을 지원합니다.

- 제안된 방법은 효과적이며 작업 간에 일반화되며, 시연 부담을 크게 줄입니다.

---

*Generated on 2025-09-18 17:04:42*