---
keywords:
  - Post-Quantum Resilience
  - TPM-based Remote Attestation
  - IoT Audio Classification
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:04:49.960531",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Post-Quantum Resilience",
    "TPM-based Remote Attestation",
    "IoT Audio Classification"
  ],
  "rejected_keywords": [
    "End-to-End Encryption"
  ],
  "similarity_scores": {
    "Post-Quantum Resilience": 0.82,
    "TPM-based Remote Attestation": 0.79,
    "IoT Audio Classification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework

**Korean Title:** 사물인터넷 오디오 분류 장치의 보안을 강화하기 위한 위협 모델링: 보안 프로토콜 프레임워크 하에서

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Post-Quantum Resilience|Post-Quantum Resilience]]
**⚡ Unique Technical**: [[keywords/TPM-based Remote Attestation|TPM-based Remote Attestation]], [[keywords/IoT Audio Classification|IoT Audio Classification]]

## 🔗 유사한 논문
- [[The Cybersecurity of a Humanoid Robot_20250918|The Cybersecurity of a Humanoid Robot]] (80.5% similar)
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (80.3% similar)
- [[Cybersecurity AI_ Humanoid Robots as Attack Vectors_20250918|Cybersecurity AI Humanoid Robots as Attack Vectors]] (78.8% similar)
- [[Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (78.6% similar)
- [[Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting_20250918|Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting]] (78.0% similar)

## 📋 저자 정보

**Authors:** Sergio Benlloch-Lopez, Miquel Viel-Vazquez, Javier Naranjo-Alcazar, Jordi Grau-Haro, Pedro Zuccarello

## 📄 Abstract (원문)

The rapid proliferation of IoT nodes equipped with microphones and capable of
performing on-device audio classification exposes highly sensitive data while
operating under tight resource constraints. To protect against this, we present
a defence-in-depth architecture comprising a security protocol that treats the
edge device, cellular network and cloud backend as three separate trust
domains, linked by TPM-based remote attestation and mutually authenticated TLS
1.3. A STRIDE-driven threat model and attack-tree analysis guide the design. At
startup, each boot stage is measured into TPM PCRs. The node can only decrypt
its LUKS-sealed partitions after the cloud has verified a TPM quote and
released a one-time unlock key. This ensures that rogue or tampered devices
remain inert. Data in transit is protected by TLS 1.3 and hybridised with Kyber
and Dilithium to provide post-quantum resilience. Meanwhile, end-to-end
encryption and integrity hashes safeguard extracted audio features. Signed,
rollback-protected AI models and tamper-responsive sensors harden firmware and
hardware. Data at rest follows a 3-2-1 strategy comprising a solid-state drive
sealed with LUKS, an offline cold archive encrypted with a hybrid post-quantum
cipher and an encrypted cloud replica. Finally, we set out a plan for
evaluating the physical and logical security of the proposed protocol.

## 🔍 Abstract (한글 번역)

IoT 노드의 급속한 확산은 마이크로폰을 장착하고 장치 내에서 오디오 분류를 수행할 수 있는 기능을 갖추고 있어, 민감한 데이터를 노출시키면서도 제한된 자원 환경에서 운영됩니다. 이를 방지하기 위해, 우리는 엣지 장치, 셀룰러 네트워크, 클라우드 백엔드를 세 개의 별도 신뢰 도메인으로 취급하는 보안 프로토콜을 포함한 심층 방어 아키텍처를 제시합니다. 이들은 TPM 기반 원격 검증과 상호 인증된 TLS 1.3을 통해 연결됩니다. STRIDE 기반의 위협 모델과 공격 트리 분석이 설계를 안내합니다. 부팅 시, 각 부팅 단계는 TPM PCR에 측정됩니다. 노드는 클라우드가 TPM 쿼트를 검증하고 일회용 잠금 해제 키를 제공한 후에만 LUKS로 봉인된 파티션을 해독할 수 있습니다. 이는 악의적이거나 변조된 장치가 비활성 상태로 유지되도록 보장합니다. 전송 중인 데이터는 TLS 1.3에 의해 보호되며, Kyber와 Dilithium으로 하이브리드화되어 양자 내성(post-quantum resilience)을 제공합니다. 한편, 종단 간 암호화와 무결성 해시는 추출된 오디오 특징을 보호합니다. 서명되고 롤백 보호된 AI 모델과 변조 반응형 센서는 펌웨어와 하드웨어를 강화합니다. 저장된 데이터는 LUKS로 봉인된 솔리드 스테이트 드라이브, 하이브리드 포스트-퀀텀 암호로 암호화된 오프라인 콜드 아카이브, 암호화된 클라우드 복제본으로 구성된 3-2-1 전략을 따릅니다. 마지막으로, 제안된 프로토콜의 물리적 및 논리적 보안을 평가하기 위한 계획을 제시합니다.

## 📝 요약

이 논문은 마이크가 장착된 IoT 노드의 오디오 분류 과정에서 발생하는 민감한 데이터 보호를 위해 제안된 다층 방어 아키텍처를 소개합니다. 이 아키텍처는 엣지 장치, 셀룰러 네트워크, 클라우드 백엔드를 각각의 신뢰 도메인으로 구분하고, TPM 기반 원격 인증 및 상호 인증된 TLS 1.3을 통해 연결합니다. STRIDE 기반의 위협 모델과 공격 트리 분석을 통해 설계가 진행되었습니다. 부팅 시 각 단계는 TPM PCR에 측정되며, 클라우드가 TPM 인증을 확인하고 일회용 해제 키를 제공해야만 LUKS로 봉인된 파티션을 해제할 수 있습니다. TLS 1.3과 Kyber, Dilithium을 활용한 하이브리드 방식으로 데이터 전송 중 보안을 강화하고, 오디오 특징의 종단 간 암호화와 무결성 해시를 통해 데이터를 보호합니다. AI 모델과 센서는 서명 및 롤백 보호와 변조 반응 기능을 갖추고 있으며, 데이터는 LUKS로 봉인된 SSD, 하이브리드 양자 내성 암호로 암호화된 오프라인 아카이브, 암호화된 클라우드 복제본을 포함한 3-2-1 전략을 따릅니다. 마지막으로, 제안된 프로토콜의 물리적 및 논리적 보안 평가 계획을 제시합니다.

## 🎯 주요 포인트

- 1. IoT 노드의 민감한 데이터 보호를 위해 TPM 기반 원격 인증과 상호 인증된 TLS 1.3을 사용하는 방어 심층 아키텍처를 제안합니다.

- 2. STRIDE 기반 위협 모델과 공격 트리 분석을 통해 설계가 이루어졌으며, 부팅 시 각 단계가 TPM PCR에 측정됩니다.

- 3. 데이터 전송 시 TLS 1.3과 Kyber 및 Dilithium을 혼합하여 양자 내성 보안을 제공하며, 오디오 특징은 종단 간 암호화와 무결성 해시로 보호됩니다.

- 4. AI 모델과 센서는 서명 및 롤백 보호를 통해 펌웨어와 하드웨어의 보안을 강화합니다.

- 5. 데이터 저장 시 LUKS로 봉인된 SSD, 하이브리드 양자 후 암호로 암호화된 오프라인 아카이브, 암호화된 클라우드 복제본을 포함한 3-2-1 전략을 따릅니다.

---

*Generated on 2025-09-20 05:46:49*