---
keywords:
  - Convolutional Neural Networks
  - Neural Networks
  - Adversarial Attacks
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.15454
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:34:17.605018",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convolutional Neural Networks",
    "Neural Networks",
    "Adversarial Attacks"
  ],
  "rejected_keywords": [
    "Local Robustness Verification"
  ],
  "similarity_scores": {
    "Convolutional Neural Networks": 0.8,
    "Neural Networks": 0.85,
    "Adversarial Attacks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Mini-Batch Robustness Verification of Deep Neural Networks

**Korean Title:** 딥 뉴럴 네트워크의 미니 배치 견고성 검증

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Deep Neural Networks]]
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|Convolutional Networks]], [[keywords/Adversarial Attacks|Adversarial Attacks]]

## 🔗 유사한 논문
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.3% similar)
- [[Communication-Efficient and Privacy-Adaptable Mech_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (78.1% similar)
- [[NavMoE Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (77.7% similar)
- [[MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (77.6% similar)
- [[Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision An Information-Theoretic Impossibility]] (77.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15454v2 Announce Type: replace 
Abstract: Neural network image classifiers are ubiquitous in many safety-critical applications. However, they are susceptible to adversarial attacks. To understand their robustness to attacks, many local robustness verifiers have been proposed to analyze $\epsilon$-balls of inputs. Yet, existing verifiers introduce a long analysis time or lose too much precision, making them less effective for a large set of inputs. In this work, we propose a new approach to local robustness: group local robustness verification. The key idea is to leverage the similarity of the network computations of certain $\epsilon$-balls to reduce the overall analysis time. We propose BaVerLy, a sound and complete verifier that boosts the local robustness verification of a set of $\epsilon$-balls by dynamically constructing and verifying mini-batches. BaVerLy adaptively identifies successful mini-batch sizes, accordingly constructs mini-batches of $\epsilon$-balls that have similar network computations, and verifies them jointly. If a mini-batch is verified, all its $\epsilon$-balls are proven robust. Otherwise, one $\epsilon$-ball is suspected as not being robust, guiding the refinement. BaVerLy leverages the analysis results to expedite the analysis of that $\epsilon$-ball as well as the analysis of the mini-batch with the other $\epsilon$-balls. We evaluate BaVerLy on fully connected and convolutional networks for MNIST and CIFAR-10. Results show that BaVerLy scales the common one by one verification by 2.3x on average and up to 4.1x, in which case it reduces the total analysis time from 24 hours to 6 hours.

## 🔍 Abstract (한글 번역)

arXiv:2508.15454v2 발표 유형: 교체  
초록: 신경망 이미지 분류기는 많은 안전이 중요한 응용 분야에서 널리 사용됩니다. 그러나 이러한 분류기는 적대적 공격에 취약합니다. 공격에 대한 신경망의 강건성을 이해하기 위해, 많은 지역 강건성 검증기가 입력의 $\epsilon$-볼을 분석하기 위해 제안되었습니다. 그러나 기존의 검증기는 긴 분석 시간을 초래하거나 너무 많은 정밀도를 잃어, 많은 입력 집합에 대해 덜 효과적입니다. 본 연구에서는 지역 강건성에 대한 새로운 접근법인 그룹 지역 강건성 검증을 제안합니다. 핵심 아이디어는 특정 $\epsilon$-볼의 네트워크 계산 유사성을 활용하여 전체 분석 시간을 줄이는 것입니다. 우리는 BaVerLy라는 건전하고 완전한 검증기를 제안하며, 이는 $\epsilon$-볼 집합의 지역 강건성 검증을 미니 배치를 동적으로 구성하고 검증함으로써 향상시킵니다. BaVerLy는 성공적인 미니 배치 크기를 적응적으로 식별하고, 이에 따라 네트워크 계산이 유사한 $\epsilon$-볼의 미니 배치를 구성하고 이를 공동으로 검증합니다. 미니 배치가 검증되면, 그 안의 모든 $\epsilon$-볼이 강건함이 증명됩니다. 그렇지 않으면, 하나의 $\epsilon$-볼이 강건하지 않다고 의심되어 세분화를 안내합니다. BaVerLy는 분석 결과를 활용하여 해당 $\epsilon$-볼의 분석뿐만 아니라 다른 $\epsilon$-볼과 함께한 미니 배치의 분석을 가속화합니다. 우리는 MNIST와 CIFAR-10에 대한 완전 연결 및 컨볼루션 네트워크에서 BaVerLy를 평가합니다. 결과는 BaVerLy가 일반적인 하나씩 검증을 평균 2.3배, 최대 4.1배까지 확장하며, 이 경우 전체 분석 시간을 24시간에서 6시간으로 줄이는 것을 보여줍니다.

## 📝 요약

이 논문은 신경망 이미지 분류기의 공격에 대한 강건성을 분석하기 위해 새로운 접근법인 그룹 지역 강건성 검증을 제안합니다. 기존 검증 방법은 분석 시간이 길거나 정밀도가 떨어지는 문제가 있었으나, 제안된 BaVerLy는 네트워크 계산의 유사성을 활용해 분석 시간을 줄입니다. BaVerLy는 미니 배치를 동적으로 구성하고 검증하여, 성공적인 미니 배치 크기를 식별하고 유사한 계산을 가진 $\epsilon$-볼을 함께 검증합니다. 검증이 성공하면 해당 $\epsilon$-볼들이 강건함을 증명하며, 실패 시에는 의심되는 $\epsilon$-볼을 찾아내어 분석을 가속화합니다. MNIST와 CIFAR-10 데이터셋에 대한 실험 결과, BaVerLy는 기존의 개별 검증 방식보다 평균 2.3배, 최대 4.1배 더 효율적이며, 총 분석 시간을 24시간에서 6시간으로 단축했습니다.

## 🎯 주요 포인트

- 1. 신경망 이미지 분류기는 안전이 중요한 많은 응용 분야에서 널리 사용되지만, 적대적 공격에 취약합니다.

- 2. 기존의 지역적 강건성 검증기는 분석 시간이 길거나 정밀도가 떨어져 많은 입력 세트에 효과적이지 않습니다.

- 3. 본 연구에서는 그룹 지역 강건성 검증이라는 새로운 접근 방식을 제안하여 분석 시간을 줄입니다.

- 4. BaVerLy는 유사한 네트워크 계산을 가진 $\epsilon$-볼을 미니 배치로 구성하여 공동 검증함으로써 검증 효율을 높입니다.

- 5. BaVerLy는 MNIST와 CIFAR-10 데이터셋의 완전 연결 및 합성곱 신경망에서 평균 2.3배, 최대 4.1배의 검증 속도 향상을 보여줍니다.

---

*Generated on 2025-09-19 15:40:01*