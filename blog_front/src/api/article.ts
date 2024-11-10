import Article from "../domain/article";
import { apiClient } from "./axios";

export const getArticles = async () => {
  let res = await apiClient.get<Article[]>("/articles/approval/");
  return res.data;
};

export const getEditedArticles = async () => {
  let res = await apiClient.get<Article[]>("/articles/articles-edited/");
  return res.data;
};

export const getArticleById = async (id: number) => {
  let res = await apiClient.get<Article>(`/articles/${id}/`);
  return res.data;
};

export const createArticle = async (article: Omit<Article, "id">) => {
  let res = await apiClient.post<Article>("/article/create/", article);
  return res.data;
};

export const patchArticle = async (article: Partial<Article>) => {
  const {id, ...a} = article;
  let res = await apiClient.patch<Article>(`/article/${id}/`, a);
  return res.data;
};
