import { SubmitHandler, useForm } from "react-hook-form";
import Article from "../domain/article";
import { useMutation } from "@tanstack/react-query";
import { createArticle } from "../api/article";
import { queryClient } from "../main";
import { useNavigate } from "react-router-dom";

const AddArticleForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors: formErrors },
  } = useForm<Omit<Article, "id">>();

  const navigate = useNavigate();

  const { mutate, isError, error, isPending } = useMutation({
    mutationFn: createArticle,
    onSuccess: () => {
      queryClient.invalidateQueries();
      navigate("/articles");
    },
    onError: (error: any) => {
      console.error("Error adding article post:", error);
    },
  });

  const onSubmit: SubmitHandler<Omit<Article, "id">> = (data) => mutate(data);
  console.log(formErrors);

  return (
    <form className="w-full" onSubmit={handleSubmit(onSubmit)}>
      {isError && <p className="text-error text-center">{error.message}</p>}
      <label className="font-bold m-1">
        Title{" "}
        <span className="text-error">{formErrors?.title?.type || ""}*</span>
      </label>
      <input
        type="text"
        placeholder="Type here"
        className="input input-bordered w-full"
        {...register("title", { required: true })}
      />
      <div className="my-5"></div>
      <label className="font-bold m-1">
        Content{" "}
        <span className="text-error">{formErrors?.content?.type || ""}*</span>
      </label>
      <textarea
        className="textarea textarea-bordered w-full"
        placeholder="Content"
        {...register("content", { required: true })}></textarea>
      <div className="my-5"></div>
      <button type="submit" className="btn block ms-auto" disabled={isPending}>
        {isPending && <span className="loading loading-spinner"></span>}
        Add
      </button>
    </form>
  );
};

export default AddArticleForm;
