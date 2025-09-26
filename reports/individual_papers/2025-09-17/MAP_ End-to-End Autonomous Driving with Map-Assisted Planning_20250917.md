---
keywords:
  - Map-Assisted Planning
  - End-to-End Autonomous Driving
  - Semantic Map Features
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:51:54.927669",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Map-Assisted Planning",
    "End-to-End Autonomous Driving",
    "Semantic Map Features"
  ],
  "rejected_keywords": [
    "Trajectory Planning"
  ],
  "similarity_scores": {
    "Map-Assisted Planning": 0.82,
    "End-to-End Autonomous Driving": 0.78,
    "Semantic Map Features": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# MAP: End-to-End Autonomous Driving with Map-Assisted Planning

**Korean Title:** 지도: 지도 지원 계획을 통한 종단 간 자율 주행

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Map Features|semantic map features]]
**⚡ Unique Technical**: [[keywords/Map-Assisted Planning|map-assisted planning]], [[keywords/End-to-End Autonomous Driving|end-to-end autonomous driving]]

## 🔗 유사한 논문
- [[FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive Energy Flow Field for End-to-End Autonomous Driving]] (83.9% similar)
- [[Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (82.9% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (82.9% similar)
- [[PA-MPPI_ Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments_20250919|PA-MPPI Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments]] (82.7% similar)
- [[Meta-Optimization and Program Search using Language Models for Task and Motion Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (82.7% similar)

## 📋 저자 정보

**Authors:** Huilin Yin, Yiming Kan, Daniel Watzenig

## 📄 Abstract (원문)

In recent years, end-to-end autonomous driving has attracted increasing
attention for its ability to jointly model perception, prediction, and planning
within a unified framework. However, most existing approaches underutilize the
online mapping module, leaving its potential to enhance trajectory planning
largely untapped. This paper proposes MAP (Map-Assisted Planning), a novel
map-assisted end-to-end trajectory planning framework. MAP explicitly
integrates segmentation-based map features and the current ego status through a
Plan-enhancing Online Mapping module, an Ego-status-guided Planning module, and
a Weight Adapter based on current ego status. Experiments conducted on the
DAIR-V2X-seq-SPD dataset demonstrate that the proposed method achieves a 16.6%
reduction in L2 displacement error, a 56.2% reduction in off-road rate, and a
44.5% improvement in overall score compared to the UniV2X baseline, even
without post-processing. Furthermore, it achieves top ranking in Track 2 of the
End-to-End Autonomous Driving through V2X Cooperation Challenge of MEIS
Workshop @CVPR2025, outperforming the second-best model by 39.5% in terms of
overall score. These results highlight the effectiveness of explicitly
leveraging semantic map features in planning and suggest new directions for
improving structure design in end-to-end autonomous driving systems. Our code
is available at https://gitee.com/kymkym/map.git

## 🔍 Abstract (한글 번역)

최근 몇 년간, 종단 간(end-to-end) 자율 주행은 인식, 예측, 계획을 통합된 프레임워크 내에서 공동으로 모델링할 수 있는 능력으로 인해 점점 더 많은 주목을 받고 있습니다. 그러나 대부분의 기존 접근법은 온라인 매핑 모듈을 충분히 활용하지 못하여 경로 계획을 향상시킬 수 있는 잠재력을 크게 활용하지 못하고 있습니다. 본 논문에서는 MAP(Map-Assisted Planning)이라는 새로운 지도 보조 종단 간 경로 계획 프레임워크를 제안합니다. MAP는 세분화 기반 지도 특징과 현재 자차 상태를 명시적으로 통합하여, 계획 향상 온라인 매핑 모듈, 자차 상태 안내 계획 모듈, 그리고 현재 자차 상태에 기반한 가중치 조정기를 통해 작동합니다. DAIR-V2X-seq-SPD 데이터셋에서 수행된 실험은 제안된 방법이 L2 변위 오류를 16.6% 감소시키고, 도로 이탈률을 56.2% 감소시키며, 전체 점수를 44.5% 향상시킨다는 것을 보여줍니다. 이는 후처리 없이도 UniV2X 기준선과 비교했을 때의 결과입니다. 또한, MEIS 워크숍 @CVPR2025의 V2X 협력 도전 과제의 종단 간 자율 주행 트랙 2에서 전체 점수 측면에서 두 번째로 좋은 모델을 39.5% 초과하여 최고 순위를 달성했습니다. 이러한 결과는 계획에서 의미적 지도 특징을 명시적으로 활용하는 것의 효과를 강조하며, 종단 간 자율 주행 시스템의 구조 설계를 개선하기 위한 새로운 방향을 제시합니다. 우리의 코드는 https://gitee.com/kymkym/map.git에서 이용할 수 있습니다.

## 📝 요약

최근 자율주행 기술에서 인식, 예측, 계획을 통합하는 종단 간 접근 방식이 주목받고 있습니다. 그러나 기존 방법들은 온라인 매핑 모듈의 잠재력을 충분히 활용하지 못했습니다. 본 논문은 MAP(Map-Assisted Planning)이라는 새로운 경로 계획 프레임워크를 제안합니다. MAP은 세분화된 지도 특징과 현재 차량 상태를 통합하여 경로 계획을 개선합니다. DAIR-V2X-seq-SPD 데이터셋 실험 결과, 제안된 방법은 L2 변위 오류를 16.6% 줄이고, 도로 이탈률을 56.2% 감소시키며, 전체 점수를 44.5% 향상시켰습니다. 또한, MEIS 워크숍 @CVPR2025의 V2X 협력 도전 과제에서 2위 모델을 39.5% 앞서는 성과를 보였습니다. 이 연구는 지도 특징을 활용한 계획의 효과를 입증하며, 자율주행 시스템의 구조 설계 개선 방향을 제시합니다.

## 🎯 주요 포인트

- 1. MAP은 분할 기반의 지도 특징과 현재 자차 상태를 통합하여 경로 계획을 개선하는 새로운 지도 보조 종단 간 경로 계획 프레임워크입니다.

- 2. 제안된 MAP 방법은 L2 변위 오류를 16.6% 감소시키고, 오프로드 비율을 56.2% 감소시키며, UniV2X 기준선과 비교하여 전체 점수를 44.5% 향상시킵니다.

- 3. MAP은 MEIS 워크숍 @CVPR2025의 V2X 협력 도전 과제의 Track 2에서 종합 점수 기준으로 두 번째 모델을 39.5% 초과하여 최고 순위를 기록했습니다.

- 4. 실험 결과는 계획에서 의미적 지도 특징을 명시적으로 활용하는 것이 효과적임을 강조하며, 종단 간 자율 주행 시스템의 구조 설계 개선을 위한 새로운 방향을 제시합니다.

---

*Generated on 2025-09-20 09:23:55*