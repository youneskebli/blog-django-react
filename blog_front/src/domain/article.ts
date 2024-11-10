type Article = {
  id: number;
  title: string;
  content: string;
  status: Status
};

export type Status = "PENDING" | "APPROVED" | "REJECTED"

export default Article;

export const findArticleById = (articles: Article[], id: number) => {
  return articles.find((b) => b.id == id);
};
