---
keywords:
  - Transformer Architecture
  - Badminton Stroke-type Transformer
  - Human Pose Estimation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2502.21085
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:55:11.784772",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Badminton Stroke-type Transformer",
    "Human Pose Estimation"
  ],
  "rejected_keywords": [
    "Shuttlecock Trajectory Tracking"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.85,
    "Badminton Stroke-type Transformer": 0.8,
    "Human Pose Estimation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# BST: Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports

**Korean Title:** BST: 라켓 스포츠에서 골격 기반 동작 인식을 위한 배드민턴 스트로크 유형 변환기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer Architecture]], [[keywords/Human Pose Estimation|Human Pose Estimation]]
**⚡ Unique Technical**: [[keywords/Badminton Stroke-type Transformer|Badminton Stroke-type Transformer]]

## 🔗 유사한 논문
- [[TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (79.1% similar)
- [[Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (77.6% similar)
- [[textsc{Gen2Real} Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (77.5% similar)
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (77.2% similar)
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.21085v3 Announce Type: replace 
Abstract: Badminton, known for having the fastest ball speeds among all sports, presents significant challenges to the field of computer vision, including player identification, court line detection, shuttlecock trajectory tracking, and player stroke-type classification. In this paper, we introduce a novel video clipping strategy to extract frames of each player's racket swing in a badminton broadcast match. These clipped frames are then processed by three existing models: one for Human Pose Estimation to obtain human skeletal joints, another for shuttlecock trajectory tracking, and the other for court line detection to determine player positions on the court. Leveraging these data as inputs, we propose Badminton Stroke-type Transformer (BST) to classify player stroke-types in singles. To the best of our knowledge, experimental results demonstrate that our method outperforms the previous state-of-the-art on the largest publicly available badminton video dataset (ShuttleSet), another badminton dataset (BadmintonDB), and a tennis dataset (TenniSet). These results suggest that effectively leveraging ball trajectory is a promising direction for action recognition in racket sports.

## 🔍 Abstract (한글 번역)

arXiv:2502.21085v3 발표 유형: 교체  
초록: 배드민턴은 모든 스포츠 중에서 가장 빠른 공 속도를 자랑하며, 이는 컴퓨터 비전 분야에 있어 선수 식별, 코트 라인 감지, 셔틀콕 궤적 추적, 선수의 스트로크 유형 분류 등과 같은 상당한 도전 과제를 제시합니다. 본 논문에서는 배드민턴 방송 경기에서 각 선수의 라켓 스윙 프레임을 추출하기 위한 새로운 비디오 클리핑 전략을 소개합니다. 이렇게 클리핑된 프레임은 세 가지 기존 모델에 의해 처리됩니다: 인간 골격 관절을 얻기 위한 인간 자세 추정 모델, 셔틀콕 궤적 추적 모델, 그리고 코트 위의 선수 위치를 결정하기 위한 코트 라인 감지 모델입니다. 이러한 데이터를 입력으로 활용하여, 우리는 단식 경기에서 선수의 스트로크 유형을 분류하기 위한 배드민턴 스트로크 유형 변환기(BST)를 제안합니다. 우리가 아는 한, 실험 결과는 우리의 방법이 가장 큰 공개 배드민턴 비디오 데이터셋(ShuttleSet), 또 다른 배드민턴 데이터셋(BadmintonDB), 그리고 테니스 데이터셋(TenniSet)에서 이전의 최첨단 기술을 능가함을 보여줍니다. 이러한 결과는 공 궤적을 효과적으로 활용하는 것이 라켓 스포츠에서의 동작 인식을 위한 유망한 방향임을 시사합니다.

## 📝 요약

이 논문은 배드민턴 경기에서 선수의 라켓 스윙을 추출하기 위한 새로운 비디오 클리핑 전략을 소개합니다. 이 클립된 프레임은 인간 자세 추정, 셔틀콕 궤적 추적, 코트 라인 검출을 위한 기존 모델들로 처리됩니다. 이를 바탕으로, 단식 경기에서 선수의 스트로크 유형을 분류하는 Badminton Stroke-type Transformer (BST)를 제안합니다. 실험 결과, 이 방법이 ShuttleSet, BadmintonDB, TenniSet 등에서 기존 최고 성능을 능가함을 보여줍니다. 이는 공 궤적 활용이 라켓 스포츠의 동작 인식에 유망한 방향임을 시사합니다.

## 🎯 주요 포인트

- 1. 배드민턴 경기에서 선수의 라켓 스윙을 추출하기 위한 새로운 비디오 클리핑 전략을 제안합니다.

- 2. 클리핑된 프레임은 인간 자세 추정, 셔틀콕 궤적 추적, 코트 라인 감지를 위한 세 가지 모델로 처리됩니다.

- 3. 제안된 Badminton Stroke-type Transformer (BST)는 단식 경기에서 선수의 스트로크 유형을 분류합니다.

- 4. 실험 결과, 제안된 방법이 ShuttleSet, BadmintonDB, TenniSet 데이터셋에서 기존 최고 성능을 능가함을 보여줍니다.

- 5. 공 궤적을 효과적으로 활용하는 것이 라켓 스포츠에서의 동작 인식에 유망한 방향임을 시사합니다.

---

*Generated on 2025-09-19 16:16:58*