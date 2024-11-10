import { SubmitHandler, useForm } from "react-hook-form";
import Auth from "../domain/auth";
import { useMutation } from "@tanstack/react-query";
import { login } from "../api/auth";
import cookies from "../lib/cookies";

const Login = () => {
  const {
    register,
    handleSubmit,
    formState: { errors: formErrors },
  } = useForm<Auth>();


  const { mutate, isError, error, isPending } = useMutation({
    mutationFn: login,
    onSuccess: ({ access_token }) => {
      cookies.setCookie("access_token", access_token!, 30);
      window.location.assign("/");
    },
    onError: (error: any) => {
      console.error("Error adding blog post:", error);
    },
  });

  const onSubmit: SubmitHandler<Auth> = (data) => mutate(data);

  return (
    <div className="flex items-center justify-center h-screen">
      <form className="w-1/3" onSubmit={handleSubmit(onSubmit)}>
        {isError && <p className="text-error text-center">{error.message}</p>}
        <label className="font-bold m-1">
          Name{" "}
          <span className="text-error">{formErrors?.email?.type || ""}*</span>
        </label>
        <input
          type="text"
          placeholder="Type here"
          className="input input-bordered w-full"
          {...register("email", { required: true })}
        />
        <div className="my-5"></div>
        <label className="font-bold m-1">
          Password{" "}
          <span className="text-error">
            {formErrors?.password?.type || ""}*
          </span>
        </label>
        <input
          className="textarea textarea-bordered w-full"
          placeholder="Password"
          {...register("password", { required: true })}
        />
        <div className="my-5"></div>
        <button type="submit" className="btn block w-full" disabled={isPending}>
          {isPending && <span className="loading loading-spinner"></span>}
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;