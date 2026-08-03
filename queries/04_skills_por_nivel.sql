SELECT
  nivel,
  skill,
  COUNT(*) AS total_mencoes
FROM vagas_skills
GROUP BY nivel, skill
ORDER BY nivel, total_mencoes DESC, skill;
