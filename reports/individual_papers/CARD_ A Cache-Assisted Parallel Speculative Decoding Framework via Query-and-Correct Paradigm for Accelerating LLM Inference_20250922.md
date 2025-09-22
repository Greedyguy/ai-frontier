# CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference

**Korean Title:** CARD: 쿼리 및 수정 패러다임을 통한 캐시 지원 병렬 추측 디코딩 프레임워크로 LLM 추론 가속화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Query-and-Correct Paradigm|Query-and-Correct Paradigm]] [[keywords/specific/Speculative Decoding|Speculative Decoding]] [[keywords/broad/LLM|LLM]] [[keywords/unique/Cache-Assisted Parallel Speculative Decoding|Cache-Assisted Parallel Speculative Decoding]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Cross-Attention Speculative Decoding_20250922|Cross-Attention Speculative Decoding]] (83.2% similar) [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (82.8% similar) [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query-and-Correct Paradigm
**🔗 Specific Connectable**: Speculative Decoding
**🔬 Broad Technical**: LLM
**⭐ Unique Technical**: Cache-Assisted Parallel Speculative Decoding
## 🔗 유사한 논문
- [[2025-09-22/Cross-Attention Speculative Decoding_20250922|Cross-Attention Speculative Decoding]] (83.2% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (82.8% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (82.5% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (82.4% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE Confidence-guided Compression in Step-by-step Efficient Reasoning]] (81.8% similar)


**ArXiv ID**: [2508.04462](https://arxiv.org/abs/2508.04462)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2508.04462.pdf)


**ArXiv ID**: [2508.04462](https://arxiv.org/abs/2508.04462)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2508.04462.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cache-Assisted Parallel Decoding
**🔗 Specific Connectable**: Speculative Decoding
**⭐ Unique Technical**: CARD
**🔬 Broad Technical**: LLM

## 🏷️ 추출된 키워드



`LLM` • 

`Speculative Decoding` • 

`CARD` • 

`Cache-Assisted Parallel Decoding`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.04462v2 Announce Type: replace 
Abstract: Speculative decoding (SD), where a draft model provides multiple candidate tokens for the target model to verify in parallel, has demonstrated significant potential for accelerating LLM inference. Yet, existing SD approaches adhere to a strict draft-then-verify paradigm, enforcing a sequential process that hampers performance and constrains the draft model's capacity. Moreover, rejecting a token in the candidate sequence invalidates all subsequent tokens, leading to wasted computation during drafting. To overcome these limitations, we propose a cache-assisted parallel speculative decoding framework called CARD, which employs a novel query-and-correct paradigm. Our approach decouples drafting from verification: the draft model populates a shared cache with candidate tokens, while the target model concurrently refines the draft's trajectory. This enables inference at near-draft-speed, effectively leveraging the draft model's efficiency without additional fine-tuning. Experimental results show that CARD significantly outperforms existing state-of-the-art methods, achieving up to a 4.83x acceleration over vanilla autoregressive decoding, with no fine-tuning required for either models.

## 🔍 Abstract (한글 번역)

arXiv:2508.04462v2 발표 유형: 교체  
초록: 추론 모델이 여러 후보 토큰을 병렬로 검증할 수 있도록 초안 모델이 제공하는 추론 디코딩(Speculative Decoding, SD)은 대규모 언어 모델(LLM) 추론을 가속화하는 데 있어 상당한 잠재력을 보여주었습니다. 그러나 기존의 SD 접근법은 엄격한 초안 후 검증 패러다임을 따르며, 이는 성능을 저해하고 초안 모델의 역량을 제한하는 순차적 과정을 강요합니다. 게다가, 후보 시퀀스에서 토큰을 거부하면 이후의 모든 토큰이 무효화되어 초안 작성 중에 계산이 낭비됩니다. 이러한 한계를 극복하기 위해, 우리는 카드(CARD)라는 캐시 지원 병렬 추론 디코딩 프레임워크를 제안합니다. 이는 새로운 쿼리 및 수정 패러다임을 활용합니다. 우리의 접근법은 초안 작성과 검증을 분리합니다: 초안 모델은 후보 토큰으로 공유 캐시를 채우고, 목표 모델은 동시에 초안의 경로를 수정합니다. 이는 추가적인 미세 조정 없이 초안 속도에 가까운 추론을 가능하게 하여 초안 모델의 효율성을 효과적으로 활용합니다. 실험 결과, CARD는 기존 최첨단 방법을 크게 능가하며, 기본 자동회귀 디코딩에 비해 최대 4.83배의 가속을 달성하며, 두 모델 모두에 대해 미세 조정이 필요하지 않습니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM) 추론을 가속화하기 위한 새로운 방법인 캐시 지원 병렬 추측 디코딩(CARD)을 제안합니다. 기존의 추측 디코딩 방식은 초안 작성 후 검증하는 순차적 과정으로 인해 성능이 제한되었고, 후보 토큰의 거부 시 이후 토큰이 무효화되는 문제가 있었습니다. CARD는 초안 작성과 검증을 분리하여, 초안 모델이 후보 토큰을 캐시에 저장하고, 목표 모델이 이를 동시에 검증하여 효율성을 높입니다. 실험 결과, CARD는 기존 방법보다 최대 4.83배 빠른 추론 속도를 달성했으며, 추가적인 모델 튜닝 없이도 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트


- 1. 기존의 추측 디코딩 방식은 엄격한 초안 후 검증 절차를 따르며, 이는 성능을 저해하고 초안 모델의 역량을 제한합니다.

- 2. 제안된 CARD 프레임워크는 초안 작성과 검증을 분리하여, 초안 모델이 공유 캐시에 후보 토큰을 채우고 목표 모델이 이를 동시에 수정합니다.

- 3. CARD는 초안 속도에 가까운 추론을 가능하게 하며, 추가적인 미세 조정 없이 초안 모델의 효율성을 효과적으로 활용합니다.

- 4. 실험 결과, CARD는 기존 최첨단 방법들을 크게 능가하며, 일반적인 자기회귀 디코딩에 비해 최대 4.83배의 가속을 달성합니다.


---

*Generated on 2025-09-22 16:02:02*