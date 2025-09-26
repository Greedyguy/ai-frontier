---
keywords:
  - Fully Homomorphic Encryption
  - Privacy-Preserving Machine Learning
  - Neural Networks
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2504.17785
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:23:58.576645",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fully Homomorphic Encryption",
    "Privacy-Preserving Machine Learning",
    "Neural Networks"
  ],
  "rejected_keywords": [
    "Residue Number Systems"
  ],
  "similarity_scores": {
    "Fully Homomorphic Encryption": 0.82,
    "Privacy-Preserving Machine Learning": 0.8,
    "Neural Networks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Silenzio: Secure Non-Interactive Outsourced MLP Training

**Korean Title:** Silenzio: 안전한 비대화식 외부 위탁 MLP 훈련

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|MLP training]]
**⚡ Unique Technical**: [[keywords/Fully Homomorphic Encryption|Fully Homomorphic Encryption]]
**🚀 Evolved Concepts**: [[keywords/Privacy-Preserving Machine Learning|privacy-preserving ML]]

## 🔗 유사한 논문
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (77.2% similar)
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (76.8% similar)
- [[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (75.9% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (75.9% similar)
- [[CyberLLMInstruct A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (75.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.17785v2 Announce Type: replace 
Abstract: Outsourcing ML training to cloud-service-providers presents a compelling opportunity for resource constrained clients, while it simultaneously bears inherent privacy risks. We introduce Silenuio, the first fully non-interactive outsourcing scheme for the training of MLPs that achieves 128bit security using FHE (precisely TFHE). Unlike traditional MPC-based protocols that necessitate interactive communication between the client and server(s) or non-collusion assumptions among multiple servers, Silenzio enables the "fire-and-forget" paradigm without such assumptions. In this approach, the client encrypts the training data once, and the server performs the training without any further interaction.
  Silenzio operates entirely over low-bitwidth integer to mitigate the computational overhead inherent to FHE. Our approach features a novel low-bitwidth matrix multiplication gadget that leverages input-dependent residue number systems, ensuring that no intermediate value overflows 8bit. Starting from an RNS-to-MRNS conversion process, we propose an efficient block-scaling mechanism, which approximately shifts encrypted tensor values to their user-specified most significant bits. To instantiate the backpropagation of the error, Silenzio introduces a low-bitwidth gradient computation for the cross-entropy loss.
  We evaluate Silenzio on standard MLP training tasks regarding runtime as well as model performance and achieve similar classification accuracy as MLPs trained using PyTorch with 32bit floating-point computations. Our open-source implementation of Silenzio represents a significant advancement in privacy-preserving ML, providing a new baseline for secure and non-interactive outsourced MLP training.

## 🔍 Abstract (한글 번역)

arXiv:2504.17785v2 발표 유형: 교체  
초록: 클라우드 서비스 제공자에게 기계 학습(ML) 훈련을 외주하는 것은 자원이 제한된 클라이언트에게 매력적인 기회를 제공하지만, 동시에 본질적인 프라이버시 위험을 수반합니다. 우리는 FHE(정확히는 TFHE)를 사용하여 128비트 보안을 달성하는 MLP 훈련을 위한 최초의 완전 비대화형 외주 스키마인 Silenzio를 소개합니다. 전통적인 MPC 기반 프로토콜은 클라이언트와 서버 간의 대화형 통신이나 여러 서버 간의 비협력 가정을 필요로 하지만, Silenzio는 이러한 가정 없이 "발사 후 잊기" 패러다임을 가능하게 합니다. 이 접근 방식에서는 클라이언트가 훈련 데이터를 한 번 암호화하고, 서버가 추가적인 상호작용 없이 훈련을 수행합니다.  
Silenzio는 FHE에 내재된 계산 오버헤드를 줄이기 위해 저비트폭 정수로 전적으로 작동합니다. 우리의 접근 방식은 입력 의존적 잉여 수 체계를 활용하여 중간 값이 8비트를 초과하지 않도록 보장하는 새로운 저비트폭 행렬 곱셈 장치를 특징으로 합니다. RNS에서 MRNS로의 변환 과정을 시작으로, 우리는 암호화된 텐서 값을 사용자 지정 최상위 비트로 대략적으로 이동시키는 효율적인 블록 스케일링 메커니즘을 제안합니다. 오류의 역전파를 구현하기 위해, Silenzio는 교차 엔트로피 손실에 대한 저비트폭 그래디언트 계산을 도입합니다.  
우리는 Silenzio를 표준 MLP 훈련 작업에서 실행 시간 및 모델 성능 측면에서 평가하였으며, 32비트 부동 소수점 계산을 사용하여 PyTorch로 훈련된 MLP와 유사한 분류 정확도를 달성했습니다. Silenzio의 오픈 소스 구현은 프라이버시 보존 ML에서 중요한 발전을 나타내며, 안전하고 비대화형 외주 MLP 훈련을 위한 새로운 기준을 제공합니다.

## 📝 요약

Silenzio는 클라우드 서비스 제공자를 통한 MLP 훈련 아웃소싱을 위한 최초의 완전 비대화형 스킴으로, 128비트 보안을 FHE(TFHE 사용)를 통해 달성합니다. 기존의 MPC 기반 프로토콜과 달리, 클라이언트와 서버 간의 상호작용이나 서버 간 비협력 가정이 필요하지 않으며, 클라이언트가 훈련 데이터를 한 번 암호화하면 서버가 추가 상호작용 없이 훈련을 수행합니다. Silenzio는 저비트폭 정수 연산을 사용하여 FHE의 계산 오버헤드를 줄이고, 입력 의존적 잔여수 시스템을 활용한 새로운 저비트폭 행렬 곱셈 기법을 도입해 중간 값이 8비트를 넘지 않도록 합니다. 또한, 암호화된 텐서 값을 사용자 지정 최상위 비트로 이동시키는 효율적인 블록 스케일링 메커니즘과 저비트폭 교차 엔트로피 손실 기울기 계산을 통해 오류 역전파를 구현합니다. Silenzio는 PyTorch의 32비트 부동소수점 연산과 유사한 분류 정확도를 유지하면서도 프라이버시를 보장하는 MLP 훈련의 새로운 기준을 제시합니다.

## 🎯 주요 포인트

- 1. Silenzio는 FHE를 활용하여 128비트 보안을 달성하는 최초의 비대화형 MLP 훈련 아웃소싱 스킴입니다.

- 2. 클라이언트가 훈련 데이터를 한 번 암호화하면 서버가 추가 상호작용 없이 훈련을 수행할 수 있습니다.

- 3. Silenzio는 8비트 오버플로우를 방지하기 위해 입력 의존적 잉여 수 체계를 활용한 저비트폭 행렬 곱셈 기법을 특징으로 합니다.

- 4. Silenzio는 표준 MLP 훈련 작업에서 PyTorch와 유사한 분류 정확도를 달성하며, 비대화형 아웃소싱 MLP 훈련의 새로운 기준을 제공합니다.

- 5. Silenzio의 오픈 소스 구현은 프라이버시 보호 ML의 중요한 발전을 나타냅니다.

---

*Generated on 2025-09-19 16:23:09*