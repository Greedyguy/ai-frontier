---
keywords:
  - Verifiable Credentials
  - CRSet
  - Ethereum Transactions
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2501.17089
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:54:06.710296",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Verifiable Credentials",
    "CRSet",
    "Ethereum Transactions"
  ],
  "rejected_keywords": [
    "Relying Parties"
  ],
  "similarity_scores": {
    "Verifiable Credentials": 0.8,
    "CRSet": 0.78,
    "Ethereum Transactions": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# CRSet: Private Non-Interactive Verifiable Credential Revocation

**Korean Title:** CRSet: 비공개 비대화형 검증 가능한 자격 증명 폐기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Ethereum Transactions|Ethereum blob-carrying transactions]]
**⚡ Unique Technical**: [[keywords/Verifiable Credentials|Verifiable Credentials]], [[keywords/CRSet|CRSet]]

## 🔗 유사한 논문
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (76.4% similar)
- [[Privacy-Preserving Uncertainty Disclosure for Facilitating Enhanced Energy Storage Dispatch]] (75.8% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (74.4% similar)
- [[Practitioners' Perspectives on a Differential Privacy Deployment Registry_20250918|Practitioners' Perspectives on a Differential Privacy Deployment Registry]] (74.1% similar)
- [[Sample Efficient Experience Replay in Non-stationary Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (73.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.17089v3 Announce Type: replace 
Abstract: Like any digital certificate, Verifiable Credentials (VCs) require a way to revoke them in case of an error or key compromise. Existing solutions for VC revocation, most prominently Bitstring Status List, are not viable for many use cases because they may leak the issuer's activity, which in turn leaks internal business metrics. For instance, staff fluctuation through the revocation of employee IDs. We identify the protection of issuer activity as a key gap and propose a formal definition for a corresponding characteristic of a revocation mechanism. Then, we introduce CRSet, a non-interactive mechanism that trades some space efficiency to reach these privacy characteristics. For that, we provide a proof sketch. Issuers periodically encode revocation data and publish it via Ethereum blob-carrying transactions, ensuring secure and private availability. Relying Parties (RPs) can download it to perform revocation checks locally. Sticking to a non-interactive design also makes adoption easier because it requires no changes to wallet agents and exchange protocols. We also implement and empirically evaluate CRSet, finding its real-world behavior to match expectations. One Ethereum blob fits revocation data for about 170k VCs.

## 🔍 Abstract (한글 번역)

arXiv:2501.17089v3 발표 유형: 교체  
초록: 디지털 인증서와 마찬가지로, 검증 가능한 자격 증명(Verifiable Credentials, VCs)은 오류나 키 손상 시 이를 폐기할 수 있는 방법이 필요합니다. VC 폐기를 위한 기존 솔루션, 특히 비트스트링 상태 목록(Bitstring Status List)은 발행자의 활동을 노출시켜 내부 비즈니스 지표를 유출할 수 있기 때문에 많은 사용 사례에 적합하지 않습니다. 예를 들어, 직원 ID 폐기를 통한 직원 변동. 우리는 발행자 활동 보호를 주요 격차로 식별하고, 폐기 메커니즘의 해당 특성에 대한 공식적인 정의를 제안합니다. 그런 다음, 이러한 프라이버시 특성을 달성하기 위해 일부 공간 효율성을 교환하는 비대화형 메커니즘인 CRSet을 소개합니다. 이를 위해 증명 스케치를 제공합니다. 발행자는 주기적으로 폐기 데이터를 인코딩하여 이더리움 블롭을 포함한 트랜잭션을 통해 게시하여 안전하고 비공개적으로 이용 가능하게 합니다. 의존 당사자(Relying Parties, RPs)는 이를 다운로드하여 로컬에서 폐기 검사를 수행할 수 있습니다. 비대화형 설계를 고수함으로써 지갑 에이전트 및 교환 프로토콜에 대한 변경이 필요 없으므로 채택이 용이합니다. 또한, CRSet을 구현하고 경험적으로 평가하여 실제 동작이 기대와 일치함을 확인했습니다. 하나의 이더리움 블롭은 약 17만 개의 VC에 대한 폐기 데이터를 수용할 수 있습니다.

## 📝 요약

이 논문은 Verifiable Credentials(VCs)의 효율적이고 프라이버시를 보호하는 폐기 메커니즘을 제안합니다. 기존의 Bitstring Status List 방식은 발급자의 활동을 노출하여 내부 비즈니스 지표를 유출할 수 있는 문제가 있습니다. 이를 해결하기 위해 발급자 활동 보호를 위한 새로운 특성을 정의하고, CRSet이라는 비대화형 메커니즘을 소개합니다. CRSet은 이더리움 블록체인에 폐기 데이터를 주기적으로 게시하여 보안성과 프라이버시를 보장하며, Relying Parties가 로컬에서 폐기 여부를 확인할 수 있게 합니다. 이 방식은 지갑 에이전트나 교환 프로토콜의 변경이 필요 없으므로 채택이 용이합니다. 실험 결과, CRSet은 약 17만 개의 VC 폐기 데이터를 하나의 이더리움 블롭에 담을 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. Verifiable Credentials(VCs)의 폐기를 위한 기존 솔루션은 발행자의 활동을 노출시킬 수 있어 많은 사용 사례에 적합하지 않다.

- 2. 발행자 활동 보호를 위한 폐기 메커니즘의 특성을 정의하고, 이를 위한 비대화형 메커니즘인 CRSet을 제안한다.

- 3. CRSet은 발행자가 폐기 데이터를 주기적으로 이더리움 블록체인에 게시하여 안전하고 비공개적으로 이용 가능하게 한다.

- 4. CRSet의 비대화형 설계는 지갑 에이전트와 교환 프로토콜의 변경 없이 쉽게 채택될 수 있다.

- 5. CRSet의 구현 및 실험적 평가 결과, 이더리움 블록 하나에 약 17만 개의 VC 폐기 데이터를 담을 수 있음이 확인되었다.

---

*Generated on 2025-09-19 16:22:10*