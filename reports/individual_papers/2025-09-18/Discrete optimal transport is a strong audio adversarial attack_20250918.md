# Discrete optimal transport is a strong audio adversarial attack

**Korean Title:** 이산 최적 수송은 강력한 오디오 적대적 공격입니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Anton Selitskiy|Anton Selitskiy]] [[authors/Akib Shahriyar|Akib Shahriyar]] [[authors/Jishnuraj Prakasan|Jishnuraj Prakasan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distribution Alignment

## 🔗 유사한 논문
- [[Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (77.5% similar)
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (76.5% similar)
- [[FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (76.5% similar)
- [[Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (76.4% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (76.1% similar)

## 📋 저자 정보

**Authors:** Anton Selitskiy, Akib Shahriyar, Jishnuraj Prakasan

## 📄 Abstract (원문)

In this paper, we show that discrete optimal transport (DOT) is an effective
black-box adversarial attack against modern audio anti-spoofing countermeasures
(CMs). Our attack operates as a post-processing, distribution-alignment step:
frame-level WavLM embeddings of generated speech are aligned to an unpaired
bona fide pool via entropic OT and a top-$k$ barycentric projection, then
decoded with a neural vocoder. Evaluated on ASVspoof2019 and ASVspoof5 with
AASIST baselines, DOT yields consistently high equal error rate (EER) across
datasets and remains competitive after CM fine-tuning, outperforming several
conventional attacks in cross-dataset transfer. Ablation analysis highlights
the practical impact of vocoder overlap. Results indicate that
distribution-level alignment is a powerful and stable attack surface for
deployed CMs.

## 🔍 Abstract (한글 번역)

이 논문에서는 이산 최적 수송(DOT)이 현대의 오디오 안티 스푸핑 대응책(CMs)에 대한 효과적인 블랙박스 적대적 공격임을 보여줍니다. 우리의 공격은 후처리, 분포 정렬 단계로 작동합니다: 생성된 음성의 프레임 수준 WavLM 임베딩을 엔트로피 기반 OT와 상위-$k$ 중심 투영을 통해 비연결 진본 풀에 정렬한 후, 신경 보코더로 디코딩합니다. AASIST 기준선과 함께 ASVspoof2019 및 ASVspoof5에서 평가한 결과, DOT는 데이터셋 전반에 걸쳐 일관되게 높은 동일 오류율(EER)을 나타내며, CM 미세 조정 후에도 경쟁력을 유지하며, 여러 전통적인 공격을 데이터셋 간 전이에 있어 능가합니다. 제거 분석은 보코더 중복의 실질적인 영향을 강조합니다. 결과는 분포 수준의 정렬이 배포된 CMs에 대해 강력하고 안정적인 공격 표면임을 나타냅니다.

## 📝 요약

이 논문에서는 이산 최적 수송(DOT)이 현대 오디오 스푸핑 방지 대책에 대한 효과적인 블랙박스 적대적 공격임을 보여줍니다. 이 공격은 생성된 음성의 프레임 수준 WavLM 임베딩을 진짜 음성 풀과 정렬하는 후처리 단계로 작동하며, 엔트로피 기반 OT와 상위-$k$ 중심 투영을 사용한 후 신경 보코더로 디코딩합니다. ASVspoof2019 및 ASVspoof5 데이터셋에서 AASIST 기준으로 평가한 결과, DOT는 일관되게 높은 동등 오류율(EER)을 기록했으며, CM 미세 조정 후에도 경쟁력을 유지하며 여러 기존 공격을 능가했습니다. 연구 결과는 분포 수준의 정렬이 배포된 CM에 대한 강력하고 안정적인 공격 표면임을 시사합니다.

## 🎯 주요 포인트

- 1. 이 논문은 이산 최적 수송(DOT)이 현대 오디오 안티 스푸핑 대응책(CMs)에 대한 효과적인 블랙박스 적대적 공격임을 보여준다.

- 2. 공격은 생성된 음성의 프레임 수준 WavLM 임베딩을 엔트로피 최적 수송과 상위-$k$ 중심 투영을 통해 비짝지 않은 진짜 음성 풀에 정렬한 후, 신경 보코더로 디코딩하는 방식으로 작동한다.

- 3. ASVspoof2019와 ASVspoof5 데이터셋에서 AASIST 기준으로 평가한 결과, DOT는 데이터셋 전반에 걸쳐 일관되게 높은 동등 오류율(EER)을 나타냈으며, CM 미세 조정 후에도 경쟁력을 유지하며 여러 기존 공격을 능가한다.

- 4. 절제 분석은 보코더 중첩의 실질적인 영향을 강조한다.

- 5. 결과는 분포 수준 정렬이 배포된 CMs에 대한 강력하고 안정적인 공격 표면임을 나타낸다.

---

*Generated on 2025-09-20 01:41:53*