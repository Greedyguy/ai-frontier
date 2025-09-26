---
keywords:
  - Large Language Models
  - Natural Language Processing
  - Distributed Inference
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2502.09922
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:16:00.266501",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Natural Language Processing",
    "Distributed Inference"
  ],
  "rejected_keywords": [
    "Serverless Computing"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Natural Language Processing": 0.85,
    "Distributed Inference": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# {\lambda}Scale: Enabling Fast Scaling for Serverless Large Language Model Inference

**Korean Title:** {\lambda}Scale: 서버리스 대형 언어 모델 추론을 위한 빠른 확장 지원

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Distributed Inference|Distributed Inference]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Taming Serverless Cold Starts Through OS Co-Design_20250919|Taming Serverless Cold Starts Through OS Co-Design]] (80.5% similar)
- [[ScaleCUA Scaling Open-Source Computer Use Agents with Cross-Platform Data]] (80.3% similar)
- [[Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (80.2% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.0% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.09922v2 Announce Type: replace 
Abstract: Serverless computing has emerged as a compelling solution for cloud-based model inference. However, as modern large language models (LLMs) continue to grow in size, existing serverless platforms often face substantial model startup overhead. This poses a significant challenge in efficiently scaling model instances to accommodate dynamic, bursty workloads commonly observed in real-world inference services. In this paper, we introduce {\lambda}Scale, an efficient serverless inference system to achieve fast model scaling. The key idea behind {\lambda}Scale is to leverage high-speed RDMA networks between GPU nodes for fast model multicast, while enabling distributed inference execution during model transmission -- referred to as "execute-while-load". {\lambda}Scale proposes an efficient model scaling scheme, {\lambda}Pipe, which supports adaptive model multicast and dynamically constructs execution pipelines across receiving nodes for collaborative, distributed inference. Additionally, {\lambda}Scale supports efficient model management across GPU and host memory, allowing fast scaling for models across different storage tiers. Evaluation results show that {\lambda}Scale enables fast model scaling and effectively handles load spikes, achieving up to 5x tail-latency improvement and 31.3% cost reduction compared to state-of-the-art solutions on real-world LLM inference traces.

## 🔍 Abstract (한글 번역)

arXiv:2502.09922v2 발표 유형: 교체  
초록: 서버리스 컴퓨팅은 클라우드 기반 모델 추론을 위한 매력적인 솔루션으로 부상하고 있습니다. 그러나 현대의 대형 언어 모델(LLM)이 계속해서 커짐에 따라 기존의 서버리스 플랫폼은 종종 상당한 모델 시작 오버헤드를 겪습니다. 이는 실제 추론 서비스에서 흔히 관찰되는 동적이고 급증하는 작업 부하에 맞춰 모델 인스턴스를 효율적으로 확장하는 데 큰 도전 과제가 됩니다. 본 논문에서는 빠른 모델 확장을 달성하기 위한 효율적인 서버리스 추론 시스템인 {\lambda}Scale을 소개합니다. {\lambda}Scale의 핵심 아이디어는 GPU 노드 간의 고속 RDMA 네트워크를 활용하여 빠른 모델 멀티캐스트를 수행하는 동시에 모델 전송 중에 분산 추론 실행을 가능하게 하는 "로드 중 실행" 방식을 도입하는 것입니다. {\lambda}Scale은 적응형 모델 멀티캐스트를 지원하고 수신 노드 간에 실행 파이프라인을 동적으로 구성하여 협력적이고 분산된 추론을 수행하는 효율적인 모델 확장 방식인 {\lambda}Pipe를 제안합니다. 또한, {\lambda}Scale은 GPU와 호스트 메모리 간의 효율적인 모델 관리를 지원하여 다양한 저장 계층에 걸쳐 모델을 빠르게 확장할 수 있도록 합니다. 평가 결과, {\lambda}Scale은 빠른 모델 확장을 가능하게 하고 부하 급증을 효과적으로 처리하여, 실제 LLM 추론 추적에서 최첨단 솔루션과 비교하여 최대 5배의 꼬리 지연 시간 개선과 31.3%의 비용 절감을 달성합니다.

## 📝 요약

서버리스 컴퓨팅은 클라우드 기반 모델 추론에 매력적인 솔루션으로 부상했지만, 대형 언어 모델(LLM)의 규모가 커짐에 따라 기존 서버리스 플랫폼은 모델 시작 지연 문제를 겪고 있습니다. 이를 해결하기 위해, 본 논문에서는 빠른 모델 확장을 위한 서버리스 추론 시스템인 {\lambda}Scale을 제안합니다. {\lambda}Scale은 GPU 노드 간 고속 RDMA 네트워크를 활용하여 모델 멀티캐스트를 가속화하고, 모델 전송 중 분산 추론 실행을 가능하게 하는 "execute-while-load" 방식을 도입합니다. 또한, {\lambda}Pipe라는 효율적인 모델 확장 방식을 통해 적응형 모델 멀티캐스트와 협력적 분산 추론을 위한 실행 파이프라인을 동적으로 구성합니다. 평가 결과, {\lambda}Scale은 최대 5배의 지연 시간 개선과 31.3%의 비용 절감을 달성하며, 실제 LLM 추론 작업에서 효과적으로 부하 급증을 처리합니다.

## 🎯 주요 포인트

- 1. 서버리스 컴퓨팅은 클라우드 기반 모델 추론을 위한 유망한 솔루션으로 부상하고 있다.

- 2. {\lambda}Scale은 빠른 모델 확장을 위한 효율적인 서버리스 추론 시스템으로, GPU 노드 간의 고속 RDMA 네트워크를 활용하여 모델 멀티캐스트를 가속화한다.

- 3. {\lambda}Scale은 "execute-while-load" 방식을 통해 모델 전송 중 분산 추론 실행을 가능하게 한다.

- 4. {\lambda}Pipe는 적응형 모델 멀티캐스트와 실행 파이프라인을 동적으로 구성하여 협력적이고 분산된 추론을 지원한다.

- 5. 평가 결과, {\lambda}Scale은 최대 5배의 지연 시간 개선과 31.3%의 비용 절감을 달성하며, 실제 LLM 추론 작업에서 부하 급증을 효과적으로 처리한다.

---

*Generated on 2025-09-19 16:24:00*