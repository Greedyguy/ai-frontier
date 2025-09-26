---
keywords:
  - Federated Learning
  - Optimal Transport
  - Distribution Alignment
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14444
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:44:04.091028",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Optimal Transport",
    "Distribution Alignment"
  ],
  "rejected_keywords": [
    "Sinkhorn Scaling"
  ],
  "similarity_scores": {
    "Federated Learning": 0.95,
    "Optimal Transport": 0.85,
    "Distribution Alignment": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport

**Korean Title:** FedAVOT: 연합 학습에서 마스킹된 최적 수송을 통한 정확한 분포 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Federated Learning|Federated Learning]]
**⚡ Unique Technical**: [[keywords/Optimal Transport|Optimal Transport]]
**🚀 Evolved Concepts**: [[keywords/Distribution Alignment|Distribution Alignment]]

## 🔗 유사한 논문
- [[FedDiverse Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection]] (83.9% similar)
- [[FedSSG Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (83.3% similar)
- [[Federated Learning for Deforestation Detection A Distributed Approach with Satellite Imagery]] (80.0% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.4% similar)
- [[Performance_Optimization_of_YOLO-FEDER_FusionNet_for_Robust_Drone_Detection_in_Visually_Complex_Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14444v1 Announce Type: new 
Abstract: Federated Learning (FL) allows distributed model training without sharing raw data, but suffers when client participation is partial. In practice, the distribution of available users (\emph{availability distribution} $q$) rarely aligns with the distribution defining the optimization objective (\emph{importance distribution} $p$), leading to biased and unstable updates under classical FedAvg. We propose \textbf{Fereated AVerage with Optimal Transport (\textbf{FedAVOT})}, which formulates aggregation as a masked optimal transport problem aligning $q$ and $p$. Using Sinkhorn scaling, \textbf{FedAVOT} computes transport-based aggregation weights with provable convergence guarantees. \textbf{FedAVOT} achieves a standard $\mathcal{O}(1/\sqrt{T})$ rate under a nonsmooth convex FL setting, independent of the number of participating users per round. Our experiments confirm drastically improved performance compared to FedAvg across heterogeneous, fairness-sensitive, and low-availability regimes, even when only two clients participate per round.

## 🔍 Abstract (한글 번역)

arXiv:2509.14444v1 발표 유형: 신규  
초록: 연합 학습(Federated Learning, FL)은 원시 데이터를 공유하지 않고 분산된 모델 학습을 가능하게 하지만, 클라이언트 참여가 부분적일 때 성능이 저하됩니다. 실제로, 사용 가능한 사용자들의 분포(가용성 분포 $q$)는 최적화 목표를 정의하는 분포(중요도 분포 $p$)와 거의 일치하지 않으며, 이는 전통적인 FedAvg에서 편향되고 불안정한 업데이트로 이어집니다. 우리는 \textbf{최적 수송을 이용한 연합 평균 (\textbf{FedAVOT})}을 제안하며, 이는 $q$와 $p$를 정렬하는 마스킹된 최적 수송 문제로 집계를 공식화합니다. Sinkhorn 스케일링을 사용하여, \textbf{FedAVOT}는 수송 기반 집계 가중치를 계산하며 수렴 보장을 제공합니다. \textbf{FedAVOT}는 비매끄러운 볼록 FL 설정에서 라운드당 참여 사용자 수와 무관하게 표준 $\mathcal{O}(1/\sqrt{T})$ 속도를 달성합니다. 우리의 실험은 이질적이고 공정성에 민감하며 가용성이 낮은 환경에서 FedAvg에 비해 성능이 크게 향상됨을 확인하였으며, 라운드당 두 개의 클라이언트만 참여하더라도 성능이 개선됨을 보여줍니다.

## 📝 요약

연합 학습(FL)은 원시 데이터를 공유하지 않고 분산된 모델 학습을 가능하게 하지만, 클라이언트 참여가 부분적일 때 문제가 발생합니다. 기존 FedAvg는 사용자의 가용성 분포와 최적화 목표 분포가 일치하지 않을 경우 편향되고 불안정한 업데이트를 초래합니다. 이를 해결하기 위해 우리는 최적 수송 문제를 활용한 \textbf{FedAVOT}를 제안합니다. 이 방법은 Sinkhorn 스케일링을 사용하여 수송 기반의 집계 가중치를 계산하며, 수렴 보장을 제공합니다. \textbf{FedAVOT}는 비매끄러운 볼록 FL 설정에서 표준 수렴 속도를 달성하며, 참여 사용자 수에 독립적입니다. 실험 결과, FedAvg보다 이질적이고 공정성에 민감하며 낮은 가용성 환경에서 성능이 크게 개선됨을 확인했습니다.

## 🎯 주요 포인트

- 1. 연합 학습(Federated Learning)은 원시 데이터를 공유하지 않고 분산 모델 학습을 가능하게 하지만, 클라이언트 참여가 부분적일 때 성능이 저하됩니다.

- 2. FedAVOT는 가용 사용자 분포와 최적화 목표 분포를 정렬하는 마스킹된 최적 수송 문제로 집계를 공식화하여 편향되고 불안정한 업데이트 문제를 해결합니다.

- 3. Sinkhorn 스케일링을 사용하여 FedAVOT는 수송 기반 집계 가중치를 계산하며, 수렴 보장을 제공합니다.

- 4. FedAVOT는 비매끄러운 볼록 FL 설정에서 참여 사용자 수와 무관하게 표준 수렴 속도를 달성합니다.

- 5. 실험 결과, FedAVOT는 이질적이고 공정성에 민감하며 낮은 가용성 환경에서도 FedAvg보다 성능이 크게 개선됨을 확인하였습니다.

---

*Generated on 2025-09-19 15:24:29*