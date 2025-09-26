---
keywords:
  - Vision Transformers
  - Multi-Modal Learning
  - Weight-Aware Robotic Grasping
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14143
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:36:29.678999",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Transformers",
    "Multi-Modal Learning",
    "Weight-Aware Robotic Grasping"
  ],
  "rejected_keywords": [
    "Symbolic Weight Reasoning"
  ],
  "similarity_scores": {
    "Vision Transformers": 0.82,
    "Multi-Modal Learning": 0.8,
    "Weight-Aware Robotic Grasping": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping

**Korean Title:** CLAW: 무게 인식 로봇 그랩핑을 위한 비전-언어-액션 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformers|CLIP model]], [[keywords/Multi-Modal Learning|Vision-Language-Action models]]
**⚡ Unique Technical**: [[keywords/Weight-Aware Robotic Grasping|weight-aware robotic grasping]]

## 🔗 유사한 논문
- [[GeoAware-VLA_Implicit_Geometry_Aware_Vision-Language-Action_Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (83.9% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (83.1% similar)
- [[TrajBooster_Boosting_Humanoid_Whole-Body_Manipulation_via_Trajectory-Centric_Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.5% similar)
- [[Video-Language Critic: Transferable Reward Functions for Language-Conditioned Robotics]] (82.5% similar)
- [[PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models]] (81.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14143v1 Announce Type: new 
Abstract: Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $\pi_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$\pi_0$ and fine-tuned $\pi_0$ models. We have uploaded the videos as supplementary materials.

## 🔍 Abstract (한글 번역)

arXiv:2509.14143v1 발표 유형: 새로운
초록: 최근에 등장한 Vision-language-action (VLA) 모델은 로봇 제어에 대한 유망한 패러다임으로 나타나며, 자연어 명령을 시각 운동 작업으로 연결하는 엔드 투 엔드 정책을 가능하게 합니다. 그러나 현재의 VLA는 종종 숫자적 임계값을 기반으로 중지하는 등 정확한 작업 제약 조건을 충족시키기 어렵다는 문제가 있습니다. 이는 그들의 관찰-행동 매핑이 훈련 데이터에 의해 암시적으로 형성되고 조건 모니터링을 위한 명시적 메커니즘이 부족하기 때문입니다. 본 연구에서는 CLAW (CLIP-Language-Action for Weight)라는 프레임워크를 제안합니다. 이 프레임워크는 조건 평가를 행동 생성으로부터 분리합니다. CLAW는 가벼운 프롬프트 생성기로서 미세 조정된 CLIP 모델을 활용하며, 이 모델은 저울의 디지털 출력을 지속적으로 모니터링하고 작업별 무게 임계값에 기반한 이산적 지시사항을 생성합니다. 이러한 프롬프트는 $\pi_0$라는 흐름 기반 VLA 정책에 의해 소비되며, 이 정책은 다중 시점 카메라 관측값과 프롬프트를 통합하여 연속적인 로봇 작업을 생성합니다. 이 설계는 CLAW가 상징적 무게 추론과 고주파수 시각 운동 제어를 결합할 수 있도록 합니다. 우리는 CLAW를 단일 물체 잡기 및 이중 팔 조작이 필요한 혼합 물체 작업과 같은 세 가지 실험 설정에서 유효성을 검증했습니다. 모든 조건에서 CLAW는 무게 인식 행동을 신뢰성 있게 실행하고 원시-$\pi_0$ 및 미세 조정된 $\pi_0$ 모델을 능가합니다. 우리는 보조 자료로 비디오를 업로드했습니다.

## 📝 요약

로봇 제어를 위한 비전-언어-행동(VLA) 모델은 자연어 지시를 시각운동 행동으로 연결하는 엔드투엔드 정책을 가능하게 함. 그러나 현재 VLA는 숫자 임계값에 따라 중지하는 등 정확한 작업 제약을 충족시키기 어려움. 본 연구에서는 CLAW(CLIP-Language-Action for Weight)를 제안하여 조건 평가를 행동 생성에서 분리함. CLAW는 가벼운 프롬프트 생성기로 세밀하게 조정된 CLIP 모델을 활용하여 저울의 디지털 출력을 지속적으로 모니터링하고 작업별 무게 임계값에 따라 이산적인 지시를 생성함. 이러한 설계는 CLAW가 상징적인 무게 추론을 고주파도 시각운동 제어와 결합할 수 있도록 함. 실험 결과, CLAW는 단일 물체 잡기 및 이중 팔 조작이 필요한 혼합 물체 작업에서 안정적으로 무게 인식 행동을 수행하고 원시-$\pi_0$ 및 세밀하게 조정된 $\pi_0$ 모델을 능가함.

## 🎯 주요 포인트

- 1. 로봇 제어를 위한 비전-언어-행동(VLA) 모델이 최근에 떠오르고 있으며, CLAW는 조건 평가를 행동 생성과 분리하여 제안함.

- 2. CLAW는 CLIP 모델을 활용하여 가벼운 프롬프트 생성기로 사용하며, 무게 임계값에 따라 이산적 지시사항을 생성함.

- 3. CLAW는 심볼적 무게 추론을 고주파 비주얼모터 제어와 결합하여 가중치 인식 행동을 안정적으로 수행하며, 다양한 실험 설정에서 우수한 성능을 보임.

---

*Generated on 2025-09-18 17:17:44*