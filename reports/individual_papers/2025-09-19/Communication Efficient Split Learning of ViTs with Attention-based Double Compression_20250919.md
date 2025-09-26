---
keywords:
  - Vision Transformers
  - Attention-based Double Compression
  - Split Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15058
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:52:21.463954",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Transformers",
    "Attention-based Double Compression",
    "Split Learning"
  ],
  "rejected_keywords": [
    "Attention Mechanism"
  ],
  "similarity_scores": {
    "Vision Transformers": 0.88,
    "Attention-based Double Compression": 0.92,
    "Split Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Communication Efficient Split Learning of ViTs with Attention-based Double Compression

**Korean Title:** 비전 트랜스포머(ViTs)의 통신 효율적인 분할 학습: 주의 기반 이중 압축을 활용하여

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformers|Vision Transformers]]
**⚡ Unique Technical**: [[keywords/Attention-based Double Compression|Attention-based Double Compression]], [[keywords/Split Learning|Split Learning]]

## 🔗 유사한 논문
- [[Singular_Value_Few-shot_Adaptation_of_Vision-Language_Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (80.8% similar)
- [[A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (78.3% similar)
- [[Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation]] (77.3% similar)
- [[Search-TTA A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (77.0% similar)
- [[MCGS-SLAM A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (76.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15058v1 Announce Type: cross 
Abstract: This paper proposes a novel communication-efficient Split Learning (SL) framework, named Attention-based Double Compression (ADC), which reduces the communication overhead required for transmitting intermediate Vision Transformers activations during the SL training process. ADC incorporates two parallel compression strategies. The first one merges samples' activations that are similar, based on the average attention score calculated in the last client layer; this strategy is class-agnostic, meaning that it can also merge samples having different classes, without losing generalization ability nor decreasing final results. The second strategy follows the first and discards the least meaningful tokens, further reducing the communication cost. Combining these strategies not only allows for sending less during the forward pass, but also the gradients are naturally compressed, allowing the whole model to be trained without additional tuning or approximations of the gradients. Simulation results demonstrate that Attention-based Double Compression outperforms state-of-the-art SL frameworks by significantly reducing communication overheads while maintaining high accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2509.15058v1 발표 유형: 교차  
초록: 이 논문은 주의 기반 이중 압축(ADC)이라는 새로운 통신 효율적인 분할 학습(SL) 프레임워크를 제안하며, 이는 SL 훈련 과정에서 중간 비전 트랜스포머 활성화를 전송하는 데 필요한 통신 오버헤드를 줄입니다. ADC는 두 가지 병렬 압축 전략을 통합합니다. 첫 번째 전략은 마지막 클라이언트 계층에서 계산된 평균 주의 점수를 기반으로 유사한 샘플의 활성화를 병합합니다. 이 전략은 클래스에 구애받지 않으며, 일반화 능력을 잃지 않으면서도 서로 다른 클래스를 가진 샘플도 병합할 수 있습니다. 두 번째 전략은 첫 번째 전략을 따르며 가장 의미 없는 토큰을 버려 통신 비용을 더욱 줄입니다. 이러한 전략을 결합하면 순방향 패스에서 전송하는 양을 줄일 수 있을 뿐만 아니라, 그래디언트도 자연스럽게 압축되어 추가 조정이나 그래디언트 근사 없이 전체 모델을 훈련할 수 있습니다. 시뮬레이션 결과에 따르면 주의 기반 이중 압축은 통신 오버헤드를 크게 줄이면서 높은 정확도를 유지하여 최첨단 SL 프레임워크를 능가합니다.

## 📝 요약

이 논문은 주의 기반 이중 압축(ADC)이라는 새로운 통신 효율적인 분할 학습(SL) 프레임워크를 제안합니다. ADC는 중간 비전 트랜스포머 활성화 전송 시의 통신 오버헤드를 줄입니다. 첫 번째 압축 전략은 마지막 클라이언트 레이어에서 계산된 평균 주의 점수를 기반으로 유사한 샘플의 활성화를 병합하며, 이는 클래스에 구애받지 않고 일반화 능력을 유지합니다. 두 번째 전략은 덜 중요한 토큰을 버려 통신 비용을 추가로 감소시킵니다. 이 두 전략을 결합하면 순방향 패스에서 전송량을 줄이고, 자연스럽게 그래디언트도 압축되어 추가 조정 없이 모델을 훈련할 수 있습니다. 시뮬레이션 결과, ADC는 통신 오버헤드를 크게 줄이면서 높은 정확도를 유지하여 기존 SL 프레임워크보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Attention-based Double Compression(ADC)는 중간 Vision Transformers 활성화 전송 시 통신 오버헤드를 줄이는 새로운 Split Learning(SL) 프레임워크입니다.

- 2. ADC는 두 가지 병렬 압축 전략을 포함하며, 첫 번째 전략은 클래스에 관계없이 유사한 샘플의 활성화를 병합하여 일반화 능력을 유지합니다.

- 3. 두 번째 전략은 첫 번째 전략을 따르며, 의미가 적은 토큰을 버려 통신 비용을 추가로 줄입니다.

- 4. 이러한 전략을 결합하면 순방향 패스에서 전송량이 줄어들 뿐만 아니라, 기울기도 자연스럽게 압축되어 추가적인 튜닝 없이 모델을 훈련할 수 있습니다.

- 5. 시뮬레이션 결과, ADC는 높은 정확도를 유지하면서 통신 오버헤드를 크게 줄여 기존의 SL 프레임워크를 능가합니다.

---

*Generated on 2025-09-19 15:05:04*