type Article = {
  id: number;
  title: string;
  content: string;
};

export default Article;

export const findArticleById = (articles: Article[], id: number) => {
  return articles.find((b) => b.id == id);
};
