import { useState } from "react";
import Article from "../domain/article";
import { useMutation } from "@tanstack/react-query";
import { patchArticle } from "../api/article";
import { queryClient } from "../main";

const EditArticle = ({ article }: { article: Article }) => {
  const [title, setTitle] = useState(article?.title);
  const [content, setContent] = useState(article?.content);

  const {
    mutate,
    isError: updateIsError,
    error: updateError,
    isPending,
  } = useMutation({
    mutationFn: () => patchArticle({
      title,
      content,
      id: article.id
    }),
    onSuccess: () => {
      queryClient.invalidateQueries();
    },
    onError: (error: any) => {
      console.error("Error adding article post:", error);
    },
  });

  return (
    <>
      <div className="flex items-center gap-4 mb-10 w-[5rem]">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="input text-3xl font-bold full"
        />
        {article.title !== title && (
          <button
            onClick={() =>
              mutate({
                title,
              })
            }
            disabled={isPending}
            className="btn btn-square">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
          </button>
        )}
      </div>

      <div className="flex items-start gap-4">
        <textarea
          rows={15}
          value={content}
          onChange={(e) => setContent(e.target.value)}
          className="text-xl textarea w-full"></textarea>
        {article.content !== content && (
          <button
            disabled={isPending}
            onClick={() =>
              mutate({
                content,
              })
            }
            className="btn btn-square">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
          </button>
        )}
      </div>
      {updateIsError && (
        <div className="toast">
          <div role="alert" className="alert alert-error">
            <span>Update failed</span>
          </div>
        </div>
      )}
    </>
  );
};

export default EditArticle;
