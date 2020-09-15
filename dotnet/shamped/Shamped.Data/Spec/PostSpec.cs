using Shamped.Data.Entities;
using Shamped.Data.Infrastructure;

namespace Shamped.Data.Spec
{
    public class PostSpec : BaseSpecification<PostEntity>
    {
        public PostSpec(int year, int month = 0) :
            base(p => p.PublishedAt.Value.Year == year &&
                      (month == 0 || p.PublishedAt.Value.Month == month))
        {
            // Fix #313: Filter out unpublished posts
            AddCriteria(p => p.Published && !p.Deleted);

            //AddInclude(post => post.Include(p => p.PostPublish));
            ApplyOrderByDescending(p => p.PublishedAt);
        }
    }
}
