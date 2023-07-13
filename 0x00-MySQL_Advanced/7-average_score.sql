-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_sc DECIMAL;

	SELECT AVG(score) INTO avg_sc FROM corrections WHERE user_id = user_id;
	UPDATE users SET average_score = avg_sc WHERE id = user_id;
END //
DELIMITER ;
