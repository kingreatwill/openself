using Microsoft.EntityFrameworkCore;
using Shamped.Data.Configurations;
using Shamped.Data.Entities;

namespace Shamped.Data
{
    public class ShampedDbContext : DbContext
    {
        public ShampedDbContext()
        {
        }

        public ShampedDbContext(DbContextOptions options)
            : base(options)
        {
        }

     
        public virtual DbSet<PostEntity> Post { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // base.OnModelCreating(modelBuilder);
            modelBuilder.ApplyConfiguration(new PostConfiguration());
        }
    }
}
