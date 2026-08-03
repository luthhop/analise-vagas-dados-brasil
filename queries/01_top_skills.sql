SELECT
  skill,
  COUNT(*) AS total_vagas,
  ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM vagas), 1) AS percentual_vagas
FROM vagas_skills
GROUP BY skill
ORDER BY total_vagas DESC, skill;
