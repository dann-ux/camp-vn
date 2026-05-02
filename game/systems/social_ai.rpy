init python:

    import random

    def get_social_group(n=2):
        # Start with a random kid
        group = [random.choice(all_kids)]

        while len(group) < n:
            best_candidate = None
            best_score = -999

            for candidate in all_kids:
                if candidate in group:
                    continue

                score = 0

                # Score based on relationships
                for member in group:
                    score += get_relationship(candidate, member)

                # Score based on mood similarity (optional flavor)
                for member in group:
                    score -= abs(candidate.mood - member.mood)

                if score > best_score:
                    best_score = score
                    best_candidate = candidate

            group.append(best_candidate)

        return group
